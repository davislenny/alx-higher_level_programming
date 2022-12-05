## 0x02-python-import_modules

### Learning Objectives
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function dir()
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs

### File Description
* 0-add.py: imports the function ```def add(a, b):``` from the file ```add_0.py``` and prints the result of the addition ``` 1 + 2 = 3```
* 1-calculation.py:  imports functions from the file ```calculator_1.py```, does some Maths, and prints the result
* 2-args.py: prints the number of and the list of its arguments.
> Usage:
```
#pythonsfun$ ./2-args.py Hello
1 argument
1: Hello
#pythonsfun$ /2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The 
5: Best
6: School
#pythonsfun$
```
* 3-infinite_add.py: prints the result of the addition of all arguments
* 4-hidden_discovery.py: prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc).
* 5-variable_load.py: imports the variable ```a``` from the file ```variable_load_5.py``` and prints its value.
* 100-my_calculator.py: imports all functions from the file ```calculator_1.py``` and handles basics operations.
* 101-easy_print.py: prints ```#pythoniscool```, followed by a new line, in the standard output
* 102-magic_calculation.py: Python function ```def magic_calculation(a, b):``` that does exactly the same as the following Python bytecode
![Python_Bytecode](https://user-images.githubusercontent.com/111700245/205687242-ece6181b-9b68-4fee-ae02-fd9284132c7d.PNG)
* 103-fast_alphabet.py: prints the alphabet in uppercase

### Authors
davislenny [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/home)
