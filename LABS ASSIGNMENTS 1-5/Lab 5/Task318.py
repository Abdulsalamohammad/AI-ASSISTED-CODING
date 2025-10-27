def is_armstrong(number: int) -> bool:
    digits = str(number)
    num_digits = len(digits)
    powered_values = [int(digit) ** num_digits for digit in digits]
    total = sum(powered_values)

    power_exp = " + ".join([f"{d}^{num_digits}" for d in digits])
    calc_exp = " + ".join([str(val) for val in powered_values])

    if total == number:
        message = (
            f"✅ {number} is an Armstrong number!\n"
            f"Explanation: {power_exp} = {calc_exp} = {total}"
        )
        return True, message
    else:
        message = (
            f"❌ {number} is NOT an Armstrong number.\n"
            f"Explanation: {power_exp} = {calc_exp} = {total} (≠ {number})"
        )
        return False, message


# ---------------- Main Program ----------------
while True:
    user_input = input("\nEnter a number to check (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Program ended. 👋")
        break
    
    if not user_input.isdigit():
        print("⚠️ Please enter a valid number!")
        continue

    num = int(user_input)
    _, result_message = is_armstrong(num)
    print(result_message)
