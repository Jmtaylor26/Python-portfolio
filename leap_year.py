# Leap Year Checker
#Jade Taylor
#11/6/24

#Initialize
#Functions
def is_leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        print("true")
    else:
        print("false")


#Main
is_leap_year(2024) #true
is_leap_year(1900) #false
is_leap_year(1600) #true

