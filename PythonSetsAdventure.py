print("Welcome to the Flight Comparison App")
print("First Enter 1 to start and/or reset the program: ")
print(" To find out if the flights include the same routes enter AirlineA, AirlineB, or AirlineC then enter: issubset")
print(" To find out if the flights are exactly identical enter AirlineA, AirlineB, or AirlineC  then enter: issuperset")
print(" To find out if the flights are completely different enter AirlineA, AirlineB, or AirlineC then enter: isdisjoint")

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

see_1=our_routes.intersection(competitor_routes)
see_2=our_routes.symmetric_difference(competitor_routes)
see_3=our_routes.difference(competitor_routes)


while True:
    choice=input("Enter your selection below. Press #1 to see airlines that are similiar. Press #2 to find if there are unique destinations and #3 to see if there are any different ")
    if choice=="1":
       print(see_1)
    elif choice=="2":
        print(see_2)
    elif choice=="3":
        print(see_3)
    else:
        print("invalid input")