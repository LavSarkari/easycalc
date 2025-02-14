# EasyCalc

```sh
EasyCalc is a simple Python script that provides various mathematical tricks and calculations. The script includes functions to square numbers ending with '5', multiply adjacent numbers, multiply numbers with last digits summing to 10, multiply the next number, and multiply numbers with nines.
```
<br> Tho being honest its pretty tough to code these logic but its really helpfull solving maths in real life lol, so just so i wont forget these trick i thought lets just do somthing of them :)
<br> 
<br>The main purpose is to understand how actually numbers works through codes we can just write `print(123*999)` and we will get answers in a sec but can we even come near it solving that qucikly? no! ryt? soo if you understand the logics of this code you'll be able to do it quickly, oh yes ofc theres tons of short on yt yapping abt the same trick but i made the code anyway xd 

## Features

1. **Square a number ending with '5'**
2. **Multiply two adjacent numbers**
3. **Multiply numbers with last digits summing to 10**
4. **Multiply the next number**
5. **Multiply with nines**

## How to Use

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/easycalc.git
    cd easycalc
    ```

2. **Run the script:**
    ```sh
    python easycalc.py
    ```

3. **Follow the on-screen instructions to select the desired calculation.**

## Functions and Logic

### 1. Square a number ending with '5'
- **Function:** `square_with_last_digit_five()`
- **Logic:** 
  - Extract the number without the last digit.
  - Multiply the extracted number by itself plus one.
  - Append '25' to the result.
  - Print the final result.

### 2. Multiply two adjacent numbers
- **Function:** `multiply_adjacent_numbers()`
- **Logic:**
  - Check if the difference between the two numbers is 2.
  - Calculate the mid-term.
  - Multiply the mid-term by itself and subtract 1.
  - Print the result.

### 3. Multiply numbers with last digits summing to 10
- **Function:** `multiply_numbers_with_last_digits_sum_10()`
- **Logic:**
  - Extract the last digits of both numbers.
  - Check if the sum of the last digits is 10.
  - Extract the number without the last digit.
  - Multiply the extracted number by itself plus one.
  - Append the product of the last digits to the result.
  - Print the final result.

### 4. Multiply the next number
- **Function:** `multiply_next_numbers()`
- **Logic:**
  - Check if the difference between the two numbers is 1.
  - Multiply the first number by itself and add the first number.
  - Print the result.

### 5. Multiply with nines
- **Function:** `multipline()](http://_vscodecontentref_/4`
- **Logic:**
  - Convert the first number to a list of digits.
  - Subtract each digit from 9 and store the result in a list.
  - Convert the result list back to a string.
  - Check if the length of the two numbers is the same.
  - If not, pad the shorter number with zeros.
  - Print the final result.

## Main Menu
- **Function:** `main()`
- **Logic:**
  - Display a menu with options to select the desired calculation.
  - Execute the corresponding function based on user input.
  - Provide an option to exit the script.

## Example Usage

```sh
----------------
TrickCalc
----------------
1. Square a number ending with '5'
2. Multiply two adjacent numbers
3. Multiply numbers with last digits summing to 10
4. Multiply adjacent numbers
5. Multiply with nines
6. Exit
----------------
Enter your choice: 1
Enter any number ending with '5' to get its square: 25
----------------
The square of 25 is 625.
----------------
