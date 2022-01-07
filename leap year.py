def is_leap(year):
   return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
year = int(input("enter the year: "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
