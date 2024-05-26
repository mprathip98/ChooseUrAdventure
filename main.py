welcome = input("Do you want to play this game? yes to continue ").lower()
if welcome != "yes":
    print("That's alright")
    quit()


q1 = input("You are in abandoned island during a nuclear war. You see a plane nearby. Do you want to approach it or stay back?")
if q1 == "yes":
    q2 = input("You see food, drinks, and a bed. You stay there for the night. You wake up the next morning and hear a sound outside. Do you want to go outside(yes) or stay inside(no)?")
    if q2 == "yes":
        print("That sound was a nuclear bomb from a distance. You go outside and the rays kill you!")
        quit()
    else:
        q3 = input("You find a secret path to the ground at the end of the plane. Go down or no")
        if q3 == "yes":
            print("You go through the tunnel and find a ship sailing. You call for help and you get rescued.")
        else:
            print("You run out of food and die in the plane.")
else:
    print("Hungry boars attack you from behind and you die")
    quit()