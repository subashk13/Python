import random

num=random.randint(0,100)
attempt=0
print("NUMBER GUESSING GAME")
while True:
    try:
        guess=(int(input("Guess The Number Between 0 to 100:")))
        attempt+=1
        if guess >num:
            print("TOO HIGH")
        elif guess<num:
            print("TOO LOW")
        else:
            print("CORRECT GUESS")
            print(f"Attempts", attempt)
            break
    except ValueError:
        print("Enter Valid Number")