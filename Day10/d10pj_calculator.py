# Calculator
from art import logo

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2
  
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  operation_symbol = input("Pick an operation from the line above: ")
  num2 = float(input("What's the second number?: "))
  
  calculation_function = operations[operation_symbol] # function
  answer1 = calculation_function(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {answer1}")
  
  is_continue = input(f"Type 'y' to continue calculating with {answer1}, or type 'n' to exit. :")
  while is_continue == "y":
    operation_symbol = input("Pick an operation: ")
    num3 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer2 = calculation_function(answer1, num3)
    print(f"{answer1} {operation_symbol} {num3} = {answer2}")
    
    is_continue = input(f"Type 'y' to continue calculating with {answer2}, or type 'n' to exit. :")
    if is_continue == "y":
      answer1 = answer2
    else:
      calculator()

calculator()