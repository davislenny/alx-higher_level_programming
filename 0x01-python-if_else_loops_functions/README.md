## 0x01-python-if_else_loops_functions

### Learning Objectives
* How to use the ```if, if ... else``` statements
* How to use comments
* How to affect values to variables
* How to use ```while``` and ```for``` loops
* How is python's ```for``` different from ```C```'s?
* How to use the ```break``` and ```continue``` statements
* How use the ```else``` clause on loops
* How to use ```range```
* What ```pass``` does and when to use it

### File Description
* 0-positive_or_negative.py - Assigns a random signed number to the variable ```number``` each time it is executed and prints whether the number stored in the variable ```number``` is positive or negative. 
> Example:
```
#pythonsfun$ ./0-positive_or_negative.py
-4 is negative
#pythonsfun$ ./0-positive_or_negative.py
0 is zero
#pythonsfun$ ./0-positive_or_negative.py
6 is positive
```
* 1-last_digit.py - Assigns a random signed number to the variable ```number``` each time it is executed and prints the last digit of the number stored in the variable ```number```.
> Example:
```
#pythonsfun$./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
#pythonsfun$./1-last_digit.py
Last digit of 3850 is 0 and is 0
#pythonsfun$./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
```
* 2-print_alphabet.py - Prints the ASCII alphabet, in lowercase, not followed by a new line.
* 3-print_alphabt.py - Prints the ASCII alphabet except ```q``` and ```e```.
* 4-print_hexa.py - Prints all numbers from ```0``` to ```98``` in decimal and in hexadecimal.
> Example:
```
#pythonsfun$./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
...
97 = 0x61
98 = 0x62
```
* 5-print_comb2.py - Prints numbers from ```0```to ```99``` in 2 digits separated by ```", "```.
* 6-print_comb3.py - Prints all possible different combinations of two digits. ```01``` and ```10``` are considered the same combination of the two digits ```0``` and ```1```
* 7-islower.py - Checks for character lowercase character.(Prototype: ```def islower(c):```)
> Example:
```
>>> islower = __import__('7-islower').islower
>>> print("a is {}".format("lower" if islower("a") else "upper"))
a is lower
>>> print("A is {}".format("lower" if islower("A") else "upper"))
A is upper
```
* 8-uppercase.py - Prints a string in uppercase.(Prototype: ```def uppercase(str):```)
> Example:
```
>>> uppercase = __import__('8-uppercase').uppercase
>>> uppercase("best")
BEST
>>> uppercase("Best School 98 Battery street")
BEST SCHOOL 98 BATTERY STREET
```
* 9-print_last_digit.py - Prints the last digit of a number.(Prototype: ```def print_last_digit(number):```)
> Example:
```
>>> print_last_digit = __import__('9-print_last_digit').print_last_digit
>>> print_last_digit(98)
8
>>> print_last_digit(-1024)
4
```
* 10-add.py - Adds two integers and returns the result.(Prototype: ```def add(a, b):```)
> Example:
```
>>> add = __import__('10-add').add
>>> print(add(2, 3))
5
```
* 11-pow.py - Computes ```a``` to the power of ```b``` and return the value.(usage like ```add``)
* 12-fizzbuzz.py - Prints the numbers from ```1``` to ```100``` separated by a space.
```
	* For multiples of three print ```Fizz``` instead of the number and for multiples of five print ```Buzz```
	* For multiples of both three and five print ```FizzBuzz```
```
* 13-insert_number.c - A function in C that inserts a number into a sorted singly linked list.
* lists.h - Header file containing function prototypes of listint_t list.
* 100-print_tebahpla.py - Prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (```z``` in lowecase the ```Y``` in uppercase.
* 101-remove_char_at.py - Creates a copy of the string, removing the character at the position ```n```.(Prototype: ```def remove_char_at(str, n):```).
> Example:
```
>>> remove_char_at = __import__('101-remove_char_at').remove_char_at
>>> print(remove_char_at("Best School", 3))
Bes School
>>> print(remove_char_at("C is fun!", 0))
 is fun!
```
### Environment
* Language: python3 (version 3.8.5) and c
* Compiler: python3 (and gcc usin the options ```-Wall -Werror -Wextra -pedantic -std=gnu89```)
* Style guidelines: [PEP 8 ](https://peps.python.org/pep-0008/) & [Betty style](https://github.com/holbertonschool/Betty/wiki)

### Authors
davislenny







