#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """Executes a function safely.

     args:
         fct: The function to execute.
         args: The arguments for the fct function.

     Returns:
         If an error occurs - None.
         Otherwise - the result of the call to fct.
     """
    try:
        result = fct(*args)
        return result
    except (Exception, BaseException) as e:
        print(f"Exception: {e}", file=sys.stderr)
        return

def divide(a, b):
    return a / b

result = safe_function(divide, 10, 0)
if result is not None:
    print(f"Result: {result}")
else:
    print("Function execution failed.")
