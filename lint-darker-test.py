import os, sys, datetime, date, requests
import re, csv, request
import os, sys, datetime, date

def example_function():
  print("This is an example function with formatting and linting issues")
  if True:
      print("This line is indented correctly")
  else:
    print("This line is not indented correctly")
    print("This line has trailing whitespace ")
    print("This line has a long string that exceeds the maximum line length limit which is usually set to 79 or 99 characters depending on the style guide being followed in the project")
    unused_variable = 42
    unused_variable2 = 22

def another_function():
    print("Another function")
    if True:
        print("This line is fine hello")
    else:
      print("This line is not fine 123")
      print("Another line with trailing whitespace ")

example_function()
another_function()
