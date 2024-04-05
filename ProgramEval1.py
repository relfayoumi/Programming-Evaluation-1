#---------QUESTION # 1---------#
print("""\n
     \t\t\t\t.-------------------------------------------.
     \t\t\t\t|██████╗  █████╗ ██╗   ██╗ █████╗ ███╗   ██╗|
     \t\t\t\t|██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗████╗  ██║|
     \t\t\t\t|██████╔╝███████║ ╚████╔╝ ███████║██╔██╗ ██║|
     \t\t\t\t|██╔══██╗██╔══██║  ╚██╔╝  ██╔══██║██║╚██╗██║|
     \t\t\t\t|██║  ██║██║  ██║   ██║   ██║  ██║██║ ╚████║|
     \t\t\t\t|╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝|
     \t\t\t\t'-------------------------------------------'
     """)
#---------QUESTION # 2---------#
import math

#ask for sides (the third side cannot exceed the sum of the first two sides)
a = float(input("Enter side a of the triangle:\n"))
b = float(input("Enter side b of the triangle:\n"))
c = float(input("Enter side c of the triangle:\n"))
#check if the third side is greater than the sum of the first two sides
if c > a + b:
  print("Rerun the program," "the sum of the third side exceeds",
        "the sum of the first two sides.")

#math
s = (a + b + c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#print
print("The area of the triangle is:", round(area, 2), "units squared")
#---------QUESTION # 3---------#
import random

#set variables
totalPercentage = 100
totalBudget = totalbudget = int(input("\nEnter your total monthly budget:"))
food = random.randint(18, 25)
clothing = random.randint(10, 15)
rent = random.randint(40, 50)

#make sure the percent always add to 100%
entertainment = totalPercentage - (food + clothing + rent)

#variable to add the values
totalPercent = food + clothing + entertainment + rent

#print
print("These are you're monthly expenses:\n", 
      food,"%\t" , totalBudget*(food/100), "$ for food,\n",
      clothing,"%\t", totalBudget*(clothing/100), "$ for clothing,\n", 
      entertainment,"%\t", totalBudget*(entertainment/100), "$ for entertainment,\n", 
      rent,"%\t", totalBudget*(rent/100), "$ for rent.\n\n")

