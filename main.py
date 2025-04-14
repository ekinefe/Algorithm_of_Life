def main_menu():
    menu()



def menu ():
    print("Choose an algorithm:")
    print("1. Daily Planner")
    print("2. Budget Balancer")
    print("3. Meal Planner")

    sellection()

def sellection():
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        # Call Budget Balancer function
        pass
    elif choice == 3:
        # Call Meal Planner function
        pass
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main_menu()