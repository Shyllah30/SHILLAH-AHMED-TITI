print("""
container : cup = 50p
          : cone = 80p  
scoop : 1$ per scoop
toppimgs: flake = 40 p
        : chocolate sprinkle = 30p
        : strawberry coulis = 60p""")

container = input("Choose a the Container (cup/cone): ")

if container in ["cup","cone"]:
    print("valid choice")
else:
    print("invalid choice")

scoops = int(input("Enter number of scoops(1-4): "))
if  scoops <=4:
    print (" valid scoops")
else:
    print("invalid scoop")

# asking for toppings
toppings = input("flake, strawberry, chocolate sprinkle(choose any): ")









      