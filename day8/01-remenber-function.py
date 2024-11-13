def gret():
    print("Hello")
    print("Bye")
    print("Goodbye")

gret()


# USING PROPS

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Bye {name}")
    print(f"Goodbye {name}")

greet_with_name("Tomek")


## TWO PARAMS
def greet_two_params(name, location):
    print(f"Hello {name} from {location}")

greet_two_params("Tomek", "Brazil")


## KEYWORD ARGUMENTS
def greet_two_params(name, location):
    print(f"Hello {name} from {location}")

greet_two_params(name="Tomek", location="Brazil")