0x00. Python - Hello, World

General
Why Python programming is awesome
Who created Python
Who is Guido van Rossum
Where does the name ‘Python’ come from
What is the Zen of Python
How to use the Python interpreter
How to print text and variables using print
How to use strings
What are indexing and slicing in Python
What is the official Python coding style and how to check your code with pycodestyle


The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
0. Run Python file
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

. Run inline
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

2. Hello, print
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x00-python-hello_world
File: 2-print.py


4. Print float
mandatory
Score: 0.0% (Checks completed: 0.0%)
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

You can find the source code here
The output of the program should be:
Float:, followed by the float with only 2 digits
followed by a new line
You are not allowed to cast number to string
You have to use f-strings
5. Print string
mandatory
Score: 0.0% (Checks completed: 0.0%)
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

You can find the source code here
The output of the program should be:
3 times the value of str
followed by a new line
followed by the 9 first characters of str
followed by a new line
You are not allowed to use any loops or conditional statement
Your program should be maximum 5 lines long


6. Play with strings
mandatory
Score: 0.0% (Checks completed: 0.0%)
Complete this source code to print Welcome to Holberton School!

You can find the source code here
You are not allowed to use any loops or conditional statements.
You have to use the variables str1 and str2 in your new line of code
Your program should be exactly 5 lines long


7. Copy - Cut - Paste
mandatory
Score: 0.0% (Checks completed: 0.0%)
Complete this source code

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word
middle_word should contain the value of the variable word without the first and last letters
8. Create a new sentence
mandatory
Score: 0.0% (Checks completed: 0.0%)
Complete this source code to print object-oriented programming with Python, followed by a new line.

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals


9. Easter Egg
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

10. Linked list cycle
mandatory
Score: 0.0% (Checks completed: 0.0%)
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.

Prototype: int check_cycle(listint_t *list);
Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:

Only these functions are allowed: write, printf, putchar, puts, malloc, free



11. Hello, write
#advanced
Score: 0.0% (Checks completed: 0.0%)
Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

Use the function write from the sys module
You are not allowed to use print
Your script should print to stderr
Your script should exit with the status code 1


