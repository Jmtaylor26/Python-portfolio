#Jade Taylor
#1/9/25
#Parameters

def hello(Name, times):
 for i in range(times):
    print("Hello," + Name)

#Challenge 1
def calculate_area(length, width):
    print("The area equals" +str(length*width))

#Challenge 2
def discount(price,discount):
    print(str(price*((100-discount)/100)))

#Main
hello("Jade", 3)
calculate_area(10, 20)
discount(100, 50)


