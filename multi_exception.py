try:
  num=int(input("enter a number:"))
  result=100/num
  print(result)
except Valueerror:
  print("Invalid input")
except ZeroDivisionError:
  print("number cannot be zero")
