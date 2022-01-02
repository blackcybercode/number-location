# numbers = "+918306894442"
# Program to find carrier and region
# of a phone number
# import phonenumbers
# from phonenumbers import geocoder, carrier
#
# # Parsing String to Phone number
# phoneNumber = phonenumbers.parse("+918306894442")
#
# # Getting carrier of a phone number
# Carrier = carrier.name_for_number(phoneNumber, 'guj')
#
# # Getting region information
# Region = geocoder.description_for_number(phoneNumber, 'guj')
#
# # Printing the carrier and region of a phone number
# print(Carrier)
# print(Region)

from simple_colors import *

import time
import  phonenumbers
from  phonenumbers import timezone,geocoder,carrier
import time, os, sys
from bs4 import BeautifulSoup
import requests

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clearScreen():
    os.system("clear")


# typingPrint(red("welcome my tool"))
typingPrint(blue("_____ welcome my tool _____\n"))
time.sleep(2)

print(red("[1] Intagram id seen"))
print(red("[2] number locetion"))

choice = input(blue("Enter your number :"))

if choice == "1":
    # importing libraries

    x = input(blue("Enter Your username :"))

    # instagram URL
    URL = "https://www.instagram.com/{}/"


    # parse function
    def parse_data(s):

        # creating a dictionary
        data = {}

        # splitting the content
        # then taking the first part
        s = s.split("-")[0]

        # again splitting the content
        s = s.split(" ")

        # assigning the values
        data['Followers'] = s[0]
        data['Following'] = s[2]
        data['Posts'] = s[4]

        # returning the dictionary
        return data


    # scrape function
    def scrape_data(username):

        # getting the request from url
        r = requests.get(URL.format(username))

        # converting the text
        s = BeautifulSoup(r.text, "html.parser")

        # finding meta info
        meta = s.find("meta", property="og:description")

        # calling parse method
        return parse_data(meta.attrs['content'])


    # main function
    if __name__ == "__main__":
        # user name
        username = x

        # calling scrape function
        data = scrape_data(username)
        text_file = open("hacker.txt", "w")

        # printing the info
        print(data)


elif choice == "2":
    numbers=input(blue("Enter Your No. : "))
    text_file = open("hacker.txt", "w")

    text_file.write(numbers)


    phone=phonenumbers.parse(numbers)
    time=timezone.time_zones_for_number(phone)
    car=carrier.name_for_number(phone, "en")
    print(phone)
    print(time)
    print(car)
