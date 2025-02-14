def square_with_last_digit_five():
    num = int(input("Enter any number ending with '5' to get its square: "))  # Getting input from user
    fn = int(str(num)[:-1])  # Extracting the number without the last digit
    print("-" * 16)
    print("The square of", num, "is", str(fn * (fn + 1)) + '25' + ".")  # Calculating and printing the square
    print("-" * 16)

def multiply_adjacent_numbers():
    num1 = int(input("Enter first number: "))  # Getting 1st input from user
    num2 = int(input("Enter second number (make sure it only has one number gap from the first number): "))  # Getting 2nd input from user
    if num2 - 2 == num1:  # Checking if the difference between the two numbers is 2
        midterm = (num2 - 1)  # Calculating the mid-term
        print("-" * 16)
        print("Multiplications of", num1, "and", num2, "is", (midterm * midterm) - 1)  # Printing the multiplication result
        print("-" * 16)
    else:
        print("The difference between the two numbers should be 2.")  # Printing error message if the difference is not 2

def multiply_numbers_with_last_digits_sum_10():
    print("Enter two numbers whose last digits sum to 10. (e.g., 24 and 26 have 4 and 6 as last digits which sum to 10.)")
    num1 = int(input("Enter first number: "))  # Getting 1st input from user
    num2 = int(input("Enter second number: "))  # Getting 2nd input from user
    fn = int(str(num1)[-1])  # Extracting the last digit of the 1st number
    ln = int(str(num2)[-1])  # Extracting the last digit of the 2nd number
    rfn = int(str(num1)[:-1])  # Extracting the number without the last digit
    if fn + ln == 10:  # Checking if the sum of the last digits is 10
        print("-" * 16)
        print("The product of", num1, "and", num2, "is", str(rfn * (rfn + 1)) + str(fn * ln) + ".")  # Printing the product
        print("-" * 16)
    else:
            print("The sum of the last digits of the two numbers should be 10.")  # Printing error message if the sum is not 10

def multiply_next_numbers():
    num1 = int(input("Enter first number: "))  # Getting 1st input from user
    num2 = int(input("Enter second number (make sure it's the next number to the first number): "))  # Getting 2nd input from user
    if num2 - 1 == num1:  # Checking if the difference between the two numbers is 1
        print("-" * 16)
        print("Multiplications of", num1, "and", num2, "is", (num1 * num1) + num1)  # Printing the multiplication result
        print("-" * 16)
    else:
        print("The difference between the two numbers should be 1.")  # Printing error message if the difference is not 1

def multipline():
    num1 = int(input("Enter first number: "))  # Getting 1st input from user
    num2 = int(input("Enter second number (make sure it only has nines, you can have multiple nines): "))  # Getting 2nd input from user

    def int_to_list(num1):
        return [int(digit) for digit in str(num1)]  # Converting integer to list of digits

    num1_list = int_to_list(num1)

    def _loop(rterms):
        result_list = []
        for i in rterms:
            result_list.append(9 - int(i))  # Subtracting each digit from 9 and appending to result list
        return result_list

    def list_to_str(lst):
        return ''.join(map(str, lst))  # Converting list of digits back to string

    def execute(num1, num2, num1_list, _loop, list_to_str):
        if len(str(num1)) == len(str(num2)):  # Checking if the length of the two numbers is the same
            rls = list_to_str(_loop(rterms=num1_list))
            print("Multiplications of", num1, "and", num2, "is =>", str(num1 - 1) + rls)  # Printing the multiplication result
        else:
            n = len(str(num2)) - len(str(num1))
            for _ in range(n):
                num1_list.insert(0, 0)  # Padding the shorter number with zeros
            rls = list_to_str(_loop(rterms=num1_list))
            print("Multiplications of", num1, "and", num2, "is =>", str(num1 - 1) + str(int(rls) + 1))  # Printing the multiplication result

    if len(str(num1)) > len(str(num2)):
        print("Seems like you found a bug :<")
        print("The first number should have less or equal digits than the second number count of nine. If you know the trick, feel free to pull request a fix!")
    else:
        for i in int_to_list(num2):
            if i != 9:
                print("The number should have only 9s.")  # Printing error message if the number does not consist of only 9s
                break
        else:
            execute(num1, num2, num1_list, _loop, list_to_str)  # Executing the multiplication logic

def main():
    while True:
        print("-" * 16)
        print("TrickCalc")
        print("-" * 16)
        print("1. Square a number ending with '5'")
        print("2. Multiply two adjacent numbers")
        print("3. Multiply numbers with last digits summing to 10")
        print("4. Multiply adjacent numbers")
        print("5. Multiply with nines")
        print("6. Exit")
        print("-" * 16)
        choice = input("Enter your choice: ")
        if choice == '1':
            square_with_last_digit_five()
        elif choice == '2':
            multiply_adjacent_numbers()
        elif choice == '3':
            multiply_numbers_with_last_digits_sum_10()
        elif choice == '4':
            multiply_next_numbers()
        elif choice == '5':
            multipline()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()