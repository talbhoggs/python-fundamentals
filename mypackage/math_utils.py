def square(x=4):
    return x*x

def main():
    output = square() 
    print(output)

# if you see this block of code
# it means it will run only if
# this file is run directly
# if this file is imported to another file
# this will not run

if __name__ == "__main__":
    main()