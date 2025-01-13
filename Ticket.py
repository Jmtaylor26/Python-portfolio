#Name:Jade Taylor
#Date: 12/11/24

#Initialize
import turtle
t = turtle.Turtle()

#Functions

#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket
def draw_ticket(name, price, dayofweek, y_location):
    t.pencolor("blue")
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    t.goto(50, y_location +215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, y_location +215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, y_location +135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(225, y_location +15)
    t.write(price, font=("Arial", 15), align="right")

def draw_ticket1():
    print("Welcome to six flags admission!")
    Name = input("What is your name?")
    Day = input("What day would you like to attend?")
    Coupon = input("do you have a coupon?")
    age = int(input("How old are you?"))
   
    if age<=3:
        print("This Ticket is free!")
        price = 0
    if age>3 and age<=17:
        print("Your Ticket is $50 during Weekdays.")
        price = 50
    else:
        print("Your ticket is $100")
        price = 100

    if Day == "Saturday" and age>3 and age<=17:
        print("Your Ticket is $100 on Weekends without a coupon code")
        price = 100
    if Day == "Sunday" and age>3 and age<=17:
        print("Your Ticket is $100 on Weekends without a coupon code")
        price = price+100
    else:
        print("Your Ticket is $50")
        price = 50

    if Coupon == "FREEFRIDAY" and age<=17:
        print("Disregaurd all fees, you won't be charged! Enjoy free Friday!")
        price = 0
    else:
        price = 100

    if Coupon == "SUNDAY10" and Day == "Sunday" and age <=17:
        print("You get 10 dollars off of your purchase!")
        price = 90
    else:
        price = 100
        
    draw_ticket(Name, price, Day, 0)


#Main
#1. Introduction()
#2. collect the pertinent information
    #Name
    #Age
    #Day of the week
    #Coupon code
#3. Write and algorithum that determines price (if statements)
#5. Print ticket
#draw_ticket("six flags", 100, "Tuesday", 0)

draw_ticket1()
