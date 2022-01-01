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
import  phonenumbers
from  phonenumbers import timezone,geocoder,carrier
numbers=input("Enter Your No. with +__: ")
phone=phonenumbers.parse(numbers)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone, "en")
print(phone)
print(time)
print(car)
