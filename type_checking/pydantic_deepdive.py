
from datetime import datetime, UTC
from pydantic import BaseModel, ValidationError, Field, EmailStr, HttpUrl,SecretStr,ValidationInfo,computed_field,field_validator,model_validator,ConfigDict
from functools import partial
from typing import Literal,Annotated
from uuid import UUID, uuid4
import json

class User(BaseModel):
    uid: int
    username: str
    email: str
    verified_at: datetime | None = None
    bio: str = ""
    is_active: bool = True
    full_name: str | None = None

user = User(uid=123, username="Charles", email="amperc@eail.com")

# Note:
# by default pydantic does not revalidate to reassignment
# but you can change that in the configuration
# user.bio = 123

print("############################### User object\n")
print(user)

# Pydantic will see a missing field username
# user1 = User(uid=123, email="amperc@eail.com")

# dictionary and json equivalent of class
print("\n############################### dictionary equivalent\n")
print(user.model_dump()) # 
print("\n############################### json equivalent\n")
print(user.model_dump_json(indent=2))

# Note
# This has 3 errors in the user inputs
# username, email, and uid. However, pydentic
# coertion is enable by default. It will automaticly convert
# "123" to type int so the total error seen by pydentic will be
# 2 only username and email. The value "123" is converted to int
# hence no pydentic error
print("\n############################### example pydantic validation\n")
try: 
    user = User(uid="123", username=123, email=None)
except ValidationError as e:
    print(e)

# ###############################
# Different types supported by Pydentic
# and setting default value in instance creation
class BlogPost(BaseModel):
    title: str
    content: str
    view_count: int = 0
    is_published: bool = False

    # default_factory is function that gets called 
    # each time you create a new instance of BlogPost
    tags: list[str] = Field(default_factory=list) # will create a list during instance creation

    # You are allowed to not use default_factory, however it will be mutable by default (don't follow best practices)
    # which means will be shared to all instance 
    # list[str] = []

    # For fields that you want the default value be create during instance creation
    #
    # example:
    # create_at: datetime = datetime.now(UTC)
    # create_at: datetime = Field(default_factore=datetime.now(UTC))
    #
    # This example above will call once the class is define not during the instance creation
    # so this is not the solution for creat_at

    # Solution 1: Lambda
    # create_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    # solution 2: partial
    create_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))

    author_id: str | int
    status: Literal["draft", "published", "archived"] = "draft"

post = BlogPost(
    title="Getting Started with Python",
    content="Here's how to begin...",
    author_id="12345",
)
print("\n############################### BlogPost\n")
print(post)

# ###############################
# Adding constraints in the field

class UserWitConstraints(BaseModel):
    #uid: Annotated[int, Field(ge=0)]
    uid: UUID = Field(default_factory=uuid4) 
    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: EmailStr 
    verified_at: datetime | None = None
    bio: str = ""
    is_active: bool = True
    password: SecretStr | str
    full_name: str | None = None
    age: Annotated[int, Field(ge=13, le=130)]

charles = UserWitConstraints(username="Charles", email="amperc@eail.com", age=14, password="secret1234")
print("\n############################### UserWithConstraints\n")
print(charles)

# User with constraints 
print("\n############################### invalid UserWithConstraints\n")
try:
    user_cons = UserWitConstraints(
        username="csm",
        email="amper@gmail.com",
        age=12,
        password="pasdf34"
    )
except ValidationError as e:
    print(e)

# ###############################
# Custom validator

class UserCustomValidator(BaseModel):
    #uid: Annotated[int, Field(ge=0)]
    uid: UUID = Field(default_factory=uuid4) 
    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: EmailStr 
    verified_at: datetime | None = None
    bio: str = ""
    is_active: bool = True
    password: SecretStr | str
    full_name: str | None = None
    age: Annotated[int, Field(ge=13, le=130)]
    website: HttpUrl | str | None = None

    # customer validator
    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be alphanumeric (underscores allowed)")
        return v.lower()

    # customer validator
    @field_validator("website", mode="before")
    @classmethod
    def add_https(cls, v: str | None) -> str | None:
        if v and not v.startswith(("http://", "https://")):
            return f"https://{v}"
        return v

user1 = UserCustomValidator(username="charles_amper", email="amperc@eail.com", age=15, password="secret1234", website="camper")
print("\n############################### User Customer validator\n")
print(user1)
print("\n############################### User Customer validator validation example\n")
try:
    user2 = UserCustomValidator(username="21@_Charles_amper", email="amperc@eail.com", age=14, password="secret1234", website="camper.com")
    print(user2)
except ValidationError as e:
    print(e)

# ###############################
# Model validator
# used for multifield validation or the whole model validation

class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self) -> "UserRegistration":
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

try:
    registration = UserRegistration(
        email="adsfasdf@gmail.com",
        password="secret123",
        confirm_password="secret456"
    )
except ValidationError as e:
    print(e)

# ###############################
# Best practice
# 1. return the value even you are not modifying it
# 2. raise a value error. Pydantic will automatically convert it to ValidationError 
# 3. if you raise an error do not mutate the value if there is error. 
# Either return the modify value or raise an error

# ###############################
# Computed field

class UserComputedField(BaseModel):
    #uid: Annotated[int, Field(ge=0)]
    uid: UUID = Field(default_factory=uuid4) 
    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: EmailStr 
    verified_at: datetime | None = None
    bio: str = ""
    is_active: bool = True
    password: SecretStr | str
    age: Annotated[int, Field(ge=13, le=130)]
    website: HttpUrl | str | None = None

    first_name: str = ""
    last_name: str = ""
    follower_count: int = 0

    @computed_field
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

    @computed_field
    def is_influencer(self) -> bool:
        return self.follower_count >= 10000


    # custom validator
    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be alphanumeric (underscores allowed)")
        return v.lower()

    # custom validator
    @field_validator("website", mode="before")
    @classmethod
    def add_https(cls, v: str | None) -> str | None:
        if v and not v.startswith(("http://", "https://")):
            return f"https://{v}"
        return v

user4 = UserComputedField(username="charles_amper", email="amperc@eail.com", age=15, password="secret1234", website="camper")
print("\n############################### User Computed field\n")
print(user4.model_dump_json(indent=3))


# Nested Model
# use other pydantic model as field types

class UserNestedModel(BaseModel):

    model_config = ConfigDict(
        populate_by_name=True, # accept both field name and alias when loading data
        #validate_assignment=True, # validate assignment, if you reassign a field in the code pydentic will validate it again
        #strict=True, # disable coersion "123" = 123 -> this will be an error
        #extra="allow", # allow extra field not define in your model
        #frozen=True, # make model immutable once created
    )

    uid: UUID = Field(alias="id", default_factory=uuid4)
    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: EmailStr
    password: SecretStr
    website: HttpUrl | None = None
    age: Annotated[int, Field(ge=13, le=130)]
    verified_at: datetime | None = None
    bio: str = ""
    is_active: bool = True

    first_name: str = ""
    last_name: str = ""
    follower_count: int = 0

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be alphanumeric (underscores allowed)")
        return v.lower()

    @field_validator("website", mode="before")
    @classmethod
    def add_https(cls, v: str | None) -> str | None:
        if v and not v.startswith(("http://", "https://")):
            return f"https://{v}"
        return v

    @computed_field 
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username


    # mypy does NOT allow stacking decorators on top of @property. (mypy limitation)
    # Mypy limitation:
    # - No extra decorators on top of @property
    # - Pydantic computed fields are not meant to be combined with @property
    # Fix:
    # - Remove @property and use only @computed_field
    #
    # @computed_field
    # @property
    # def is_influencer(self) -> bool:
        # return self.follower_count >= 10000

    @computed_field
    def is_influencer(self) -> bool:
        return self.follower_count >= 10000

class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likes: int = 0

class BlogPostNestModel(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=200)]
    content: Annotated[str, Field(min_length=10)]
    author: UserNestedModel
    view_count: int = 0
    is_published: bool = False
    tags: list[str] = Field(default_factory=list)
    create_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    status: Literal["draft", "published", "archived"] = "draft"
    slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]

    comments: list[Comment] = Field(default_factory=list)

post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "slug": "understanding-pydantic",
    "author": {
        "username": "amperca",
        "email": "amperc@gmail.com",
        "age": 33,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}

# creating a blog post
# Ways to unpack (load the data or create data)
# 1. using double ** 
# post_nest_model = BlogPostNestModel(**post_data) # unpacking to generate blog post
# 2 model_validate
post_nest_model = BlogPostNestModel.model_validate(post_data)
print("\n############################### Nested Model \n")
print(post_nest_model.model_dump_json(indent=2))


# Serialization
# example input
### User Dictionary
user_data = {
    "id": "3bc4bf25-1b73-44da-9078-f2bb310c7374",
    "username": "Corey_Schafer",
    "email": "CoreyMSchafer@gmail.com",
    "age": "39",
    "password": "secret123",
    "notes": "Testing" # extra field
}

user_model = UserNestedModel.model_validate(user_data) # importing a dictionary
# user_model = UserNestedModel.model_validate_json(json.dumps(user_data)) # importing json
print("\n############################### User excluding fields\n")
print(user_model.model_dump_json(indent=2, by_alias=True, exclude={"password"})) # this will exclude the password in the result
print("\n############################### User including fields\n")
print(user_model.model_dump_json(indent=2, include={"username", "email"})) # this will show username and email only

# Configuring pydentic
# key/value pair define in the object

#model_config = ConfigDict(
    #populate_by_name=True, # accept both field name and alias when loading data
    #validate_assignment=True, # validate reassignment, if you reassign a field in the code pydentic will validate it again
    #strict=True, # disable coersion "123" = 123 -> this will be an error
    #extra="allow", # set extra field not define in your model
    #frozen=True, # make model immutable once created
#)