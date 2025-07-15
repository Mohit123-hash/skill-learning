def marriage_calculator():
    while True:
        age = input("Enter your age (or type 'exit' to quit): ")
        if age.lower() == 'exit':
            print("Exiting Marriage Calculator.")
            break
        try:
            age = int(age)
            if age < 0:
                print("Age cannot be negative. Try again.")
            elif age < 18:
                print("You are too young to get married.")
            elif 18 <= age < 30:
                print("You are at a common age for marriage.")
            elif 30 <= age < 60:
                print("You can still get married if you wish.")
            else:
                print("Marriage is possible at any age!")
        except ValueError:
            print("Invalid input. Please enter a valid age.")

if __name__ == "__main__":
    marriage_calculator()