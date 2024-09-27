
def q1():
  #Write Assignment code here
  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  #Write Assignment code here
  not0 = int(input("Enter an integer: "))
  print(not0 != 0)

def q3():
  #Write Assignment code here
  num = float(input("Enter a number: "))
  print(num > -1 and num < 11)

def q4():
  #Write Assignment code here
  foo = input("Input food: ")
  dri = input("Input drink: ")
  print(not foo == "pizza" or foo == "pop" and dri == "pop" or dri == "pizza")

def q5():
  #Write Assignment code here
  inte = int(input("Enter an integer: "))
  print("The integer " + str(inte) + (" is"), end = " ")
  print(int(inte % 2) == 0, end = "")
  print(".")


#Do not edit code after this
#Comment out the followwing code when running tests

# q1()
# q2()
# q3()
# q4()
# q5()
