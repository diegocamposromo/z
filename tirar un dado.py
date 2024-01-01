import random

def dado(numero):
    if numero == 1:
        print("   |   |   ")
        print("   | 0 |   ")
        print("   |   |   ")
    elif numero == 2:
        print("   |0  |   ")
        print("   |   |   ")
        print("   |  0|   ")
    elif numero == 3:
        print("   |  0|   ")
        print("   | 0 |   ")
        print("   |0  |   ")
    elif numero == 4:
        print("   |0 0|   ")
        print("   |   |   ")
        print("   |0 0|   ")
    elif numero == 5:
        print("   |0 0|   ")
        print("   | 0 |   ")
        print("   |0 0|   ")
    elif numero == 6:
        print("   |0 0|   ")
        print("   |0 0|   ")
        print("   |0 0|   ")


azar = random.randint(1, 6)


dado(azar)