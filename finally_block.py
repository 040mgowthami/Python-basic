try:
  a=input("enter a number:")
  result=a/2
  print(result)
except ZeroDivisionError:
  print("error")
finally:
  print("Done!")
