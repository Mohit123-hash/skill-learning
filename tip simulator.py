def calculate_tips(bill_amount, num_friends):
    if num_friends <= 0:
        print("Number of friends must be at least 1.")
        return

    split_amount = bill_amount / num_friends
    print(f"Total bill: ${bill_amount:.2f}")
    print(f"Number of friends: {num_friends}")
    print(f"Each friend pays: ${split_amount:.2f}")

    print("\nTip suggestions per friend:")
    for tip_percent in range(10, 51, 10):
        tip = split_amount * tip_percent / 100
        total_with_tip = split_amount + tip
        print(f"{tip_percent}% tip: Tip = ${tip:.2f}, Total = ${total_with_tip:.2f}")

if __name__ == "__main__":
    try:
        bill = float(input("Enter the total bill amount: $"))
        friends = int(input("Enter the number of friends: "))
        calculate_tips(bill, friends)
    except ValueError:
        print("Invalid input. Please enter numeric values.")