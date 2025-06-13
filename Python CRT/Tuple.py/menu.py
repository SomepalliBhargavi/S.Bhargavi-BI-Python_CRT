''#write a program 
#1) to display a menu of food items (list)
#2)create a tuple of prices with respect to food items list
#3)read the input from user for ordering the food including the Quantity
#if it exists in the menu -- confirm order, if not print a message -- order something else
#4)While billing , read no., feedback,read tip amount
#5)add 18% gst to the bill and print the bill if bill > ''

n=int(input("Enter the no.of food items : "))
list=['Gulab jamun','Biriyani','Naan','Butter Chicken','Ice cream']
Tuple=('50/-','350/-','30/-','200/-','80/-')
print(f"{list}-{Tuple}")
i=1
while(i<=n):
    fooditem=input("Enter the food item :")
    index=list.index(fooditem)
    print(f"{fooditem}-{Tuple[index]}")
    i+=1
    