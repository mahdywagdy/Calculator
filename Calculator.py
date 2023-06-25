while True:
  #1- input the first number
  while True:
    try:
      first_number = float(input("enter first number: "))
      break
    except ValueError:
      print("invaled input.please enter a numeric value")

  
  #2- input the opperation type
  while True:
    try:
      opperation = input("enter opperation type: ")
      if opperation in("+","-","/","*"):
        break
      else:  
        raise ValueError
    except ValueError:
      print("invaled opperation.Please enter +,-,/,* ")

  
  #3- input the secounf numbe
  while True:
    try:
      second_number = float(input("enter second number: "))
      if second_number==0 and opperation == "/" :
        raise ZeroDivisionError
      break
    except ValueError:
        print("invaled input.please enter a numeric value")
    except ZeroDivisionError:
      print("cannot divide by zero, please enter another numeric value")
  #4- print the result
  if opperation == "+":
    result =first_number + second_number
  elif opperation == "-":
    result =first_number - second_number
  elif opperation == "/":
   result =first_number / second_number
  elif opperation == "*":
    result =first_number * second_number
  else:
    result = None

  if result != None:
    print("Result is", result)
  else:
    print("unexcpected erorr")
    
  repeat = input("Do you want to perform another operation (y/n): ")
  if repeat == "n":
    break
      
print("Program Exited")