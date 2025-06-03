
#Welcome!
import random #This is responsible for making random selections in my function.
from PIL import Image #This allows my function to work with images.
import requests #This allows my function to work with images.
from io import BytesIO #This allows my function to work with images.
import time #This allows my function to take time before generating a response.

#This is my list of locations for my user to recieve randomly.
locations = ["https://tinyurl.com/yh5kkbus",
             "https://tinyurl.com/muc3u2pk",
             "https://tinyurl.com/mw2nuvb7",
             "https://tinyurl.com/mtbh5m7z"

]

#All of this code is a refence to what we have learned in class
#Functions
def open_image(url): #This function allows images to be used in the function below.
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()
def recommendation(): #This function allows for my user to decide whether or not they want a recommendation.
    print("welcome to vacation recommender!")
    while True:
        ans = input("would you like a recommendation?")
        if ans == "yes":
            rec = random.randint(0,4) #This selects a random image from the list I provided.
            time.sleep(1)
            print("thinking...")
            time.sleep(1)
            open_image(locations[rec])
        if ans == "no":
            print("Okay thanks anyways!")
            break

#1 Bora Bora - The official link to where I accesed this website is
# https://i.ytimg.com/vi/gSudm8JWvlQ/hqdefault.jpg
#2 Boulder Colorado - The official link to where I accesed this website is
# https://i.ytimg.com/vi/Gpb2ZYZhWPE/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFry
# q4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCDzxY0u5VjKtydWaVRgFJiov_o4Q
#3 Honolulu Hawaii - The official link to where I accesed this website is
# https://www.livebeaches.com/wp-content/uploads/2021/02/hawaii-oahu-honolulu-visit-vacation-1080x540-01.jpg
 #4 Tokyo The official link to where I accesed this website is
# https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBZUktYT5I04qIzKpDOhlUNoOOFl
# ymiou31c7OSPy_Ch0WjGzQ:https://cdn.kyushuandtokyo.org/front_assets/images_other/pref/sp/tokyo.jpg&s

#Main
recommendation()

