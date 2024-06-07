# control structures
# if ,elif, else
age=23
if age < 18:
     print ("You are an adult")
elif age > 65:
     print("You are a senior citizen")  
else:
     print("You are a youth")  
grade=80
if grade>=90:
     print("Excellent")
elif grade>=80:
     print("very good")
elif grade>=70:
     print("Good")
else:
     print ("Not Good")  
# exercise two


def get_movie_price(age):
     if age < 13:
         return 1000
     elif age >= 13 and age <= 18:
         return 500
     elif age >= 18 and age <= 64:
         return 2080
     else:
         return 5000

age = int(input("Enter your age: "))
price = get_movie_price(age)
print(f"Your movie price is: {price}")

# loops for loop and while loop
cars=["Tesla","Audi","BMW","Jeep","RangeRover"]
  # exercise   colors=["Blue", "black","aqua"]
colors =["blue","yellow","aqua"]  
for color in colors:
    print (color)
    
counting=5
while counting>=1:
    print("count 5 to 1",counting)
    counting-=1
    
# Reversing using for loop
colors = ["blue", "yellow", "aqua"]  # List of colors
reverse_color = colors[::-1]  # Reverse the list using slicing
for color in reverse_color:
    print(color)
    
    

# using while loop
colors = ["blue", "yellow", "aqua"]  # List of colors

index = len(colors) - 1  # Start with the last index
while index >= 0:
    print(colors[index])
    index -= 1



