from dataclasses import dataclass 
from tabulate import tabulate
import uuid, time, os

@dataclass
class User():
    _id:str
    _name:str
    _role:str

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name:str):
        self._name = name

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role:str):
        self._role = self.role

@dataclass
class Product():
    id:str
    name:str
    price:float
    status:str

@dataclass
class CartItem():
    product:Product
    quantity:int

class ProductService:

    def __init__(self, products:list[Product]):
        self.products = products

    def get_product(self, id:str)->Product:
        try:
            return next(item for item in self.products if item.id == id)
        except StopIteration:
            raise ValueError("Product not found")
        #for item in self.products:
            #if item.id == id:
                 #return item
        #raise ValueError("Product not found")

    def get_products(self)->list[Product]:
        return self.products

    def update_product(self):
        pass

class UserService:
    def __init__(self, users:list[User]):
        self._users = users

    @property 
    def users(self):
        return self._users
    
    def get_user_name(self, name:str):
        try: 
            user_found = next(u for u in self._users if u.name == name)
            return user_found
        except StopIteration as e:
            raise ValueError("User not found")

class ShoppingCart():

    def __init__(self, cart_items:list[CartItem], product_service:ProductService):
        self.cart_items = cart_items 
        self.product_service = product_service

    def get_products(self):
        return self.product_service.get_products()
    
    def get_cart_items(self):
        return self.cart_items

    def add_cart_item(self, product_id:str, quantity:int):
        product = self.product_service.get_product(product_id)
        cart_item = CartItem(product=product, quantity=int(quantity))
        self.cart_items.append(cart_item)
        return cart_item

    def update_cart_item(self, product_id:str, quantity:int):
        for item in self.cart_items:
           if item.product.id == product_id:
                item.quantity = int(quantity)
                return item.product
        return None

    def remove_cart_item(self, product_id:str):
        for item in self.cart_items:
           if item.product.id == product_id:
               self.cart_items.remove(item)               
               return item.product
        return None

    # move this to UIManager
    #def checkout(self):
        #for item in self.cart_items:
            #total += item.product.price * item.quantity

        #return total

    def total_cost(self):
        total = 0
        for item in self.cart_items:
            total += item.product.price * item.quantity
        return total 

class UIManager():
    def __init__(self, shoping_chart:ShoppingCart, user_service:UserService, user: User | None=None, user_action:str="1"):
        self.shoping_chart = shoping_chart
        self.user_action = user_action
        self.user_service = user_service
        self.user = user

    def show_products(self):
        self.clear_screen()
        while True:
            print("\n--- Products ---\n")
            data =  self.shoping_chart.get_products()
            print(tabulate(data, headers=["id", "name", "price", "status" ], tablefmt="presto"))
            print("\npress [1] to go back main menu")
            user_input = input("> ")
            if user_input == "1":
                break
            
    def show_cart(self):
        self.clear_screen()
        while True:
            print("\n--- Cart ---\n")
            items = self.shoping_chart.get_cart_items()

            formated_items = []
            for item in items:
                formated_items.append([item.product.id, item.product.name, item.quantity, item.product.price*item.quantity])

            if len(items) > 0:
                print(tabulate(formated_items, headers=["id", "name", "quantity", "price"], tablefmt="simple"))
            else:
                print("Chart is empty")

            print("\npress [1] to go back main menu")
            user_input = input("> ")
            if user_input == "1":
                break

    def checkout(self):
        self.clear_screen()
        while True:
            print("\n--- Checkout ---\n")
            items = self.shoping_chart.get_cart_items()

            formated_items = []
            for item in items:
                formated_items.append([item.product.id, item.product.name, item.quantity, item.product.price*item.quantity])

            if len(items) > 0:
                print(tabulate(formated_items, headers=["id", "name", "quantity", "price"], tablefmt="simple"))
                print(f"Total: {self.shoping_chart.total_cost()}")
            else:
                print("Chart is empty")

            print("\npress [1] to go back main menu")
            user_input = input("> ")
            if user_input == "1":
                break

    def add_cart_item(self):
        self.clear_screen()
        print("\n--- Add Cart item ---\n")
        try:
            product_id = input("> Enter Product Id: ")
            quantity = input("> Enter quantity: ")
            self.shoping_chart.add_cart_item(product_id=product_id, quantity=quantity)
        except ValueError as e:
            print(e)
        time.sleep(1)

    def update_cart_item(self):
        self.clear_screen()
        try:
            print("\n--- Update Cart item ---\n")
            product_id = input("> Enter Product Id: ")
            quantity = input("> Enter quantity: ")
            self.shoping_chart.update_cart_item(product_id=product_id, quantity=quantity)
        except ValueError as e:
            print(e)
        time.sleep(1)

    def remove_cart_item(self):
        self.clear_screen()
        try:
            print("\n--- Remove Cart item ---\n")
            product_id = input("> Enter Product Id: ")
            self.shoping_chart.remove_cart_item(product_id=product_id)
        except ValueError as e:
            print(e)
        time.sleep(1)
    

    def menu(self):
        self.clear_screen()
        admin_menu = "[8] Manage" if self.can_manage(self.user)  else ""
        menu = []
        menu.append(["-Menu-", "[1] products","[2] cart", "[3] add-to-cart","[4] remove-cart", "[5] update-cart","[6] checkout", "[7] logout"])
        print(tabulate(menu,
                       headers=["---- Shopping Store ----","", "","", "", "", "", f"Welcome {self.user.name} {admin_menu}"], tablefmt="simple"))
    
    def clear_screen(self):
        os.system("clear")

    def login(self):
        while True:
            try: 
                self.clear_screen()
                print("-- Login --\n")
                username = input("Enter Username: ")
                self.user = self.user_service.get_user_name(name=username)
                input("Password: ")
                break
            except ValueError as e:
                print("Invalid or Username not found")
            time.sleep(1)

    def logout(self):
        self.clear_screen()
        self.user = None    
        print("\nLogout Successfully!")
        time.sleep(1)

    def can_manage(self, user:User) -> bool:
        return user.role in ["admin"]
    
    def manage(self):
        while True:
            self.clear_screen()
            print("--- Manage ---\n")
            print("Products: [1] Add [2] Upate [3] Delete\n")
            print("User    : [4] Add [5] Upate [6] Delete\n")

            print("\npress [1] to go back main menu")
            user_input = input("> ")
            if user_input == "1":
                break


    def main(self):
        while True:
            if self.user is None:
                self.login()

            print("\n")
            self.menu()
            user_action = input("> ") 

            if(user_action == "1"):
                self.show_products()
            elif(user_action == "2"):
                self.show_cart()
            elif(user_action == "3"):
                self.add_cart_item()
            elif(user_action == "4"):
                self.remove_cart_item()
            elif(user_action == "5"):
                self.update_cart_item()
            elif(user_action == "6"):
                self.checkout()
            elif(user_action == "7"):
                self.logout()
            elif(user_action == "8"):
                if self.can_manage(self.user):
                    self.manage()

products : list[Product] = [
   Product(id="024633d3-80bc-43ce-a005-4157623922f2", name="Kettle Dumbell 10kg", price=10.5, status="active"),
   Product(id="1fd4ccda-ae06-48b5-84af-2d4f8ab1429a", name="Dumbell 10kg", price=10.5, status="active") 
]

users : list[User] = [
    User(_id=str(uuid.uuid4()),_name="Charles",_role="admin"),
    User(_id=str(uuid.uuid4()),_name="joy",_role="regular")
]

if __name__ == "__main__":

    user_service = UserService(users=users)
    product_service = ProductService(products=products)
    shopping_cart = ShoppingCart(product_service=product_service, cart_items=[])
    ui = UIManager(shoping_chart=shopping_cart,user_service=user_service)
    ui.main()

# Load data user and products in json
# add manage page
   # 1 add / update / delete user
   # 2 add / update / delete products

# add validation in adding quantity






