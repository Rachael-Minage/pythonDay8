import math
from logo_art import logo
print(logo)
# from turtle import position
# from turtle import position

# def greet():
#     print('Hey there')
#     print("Great to meet you today")
#     print("Have a good day")
# greet()
# #Function that allows for input
def greet_with_name(name):
    print(f'Hey there {name}')
    print(f"Great to meet you today {name}")
    print(f"Have a good day {name}")

greet_with_name("minage")
# Functions wit more than one input
def greet_with(name,location):
    print(f"hello {name}")
    print(f"What is it like in {location}")


greet_with("Minage","Kilifi")
# Functions with keyword arguments


print("PRIME NUMBER CHECKER")
def number_checker(number):
  prime_number = True
  for sample_number in range(2,number-1):
    if number%sample_number==0:
      prime_number=False
  if prime_number:
      print(f"{number} is a prime number")
  else:
      print(f"{number} is not a prime number")


num= int(input("Enter a number \n"))
number_checker(number= num)


# Caeser cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt and decode to decrypt")
text = input("Type your message \n")
shift= int(input("Type shift amount \n"))
print(shift)
shift= shift%25
print(shift)



# def encrypt(plain_txt, shift_amt):
#   cipher_text =""
#   for letter in plain_txt:
#     position= alphabet.index(letter)
#     new_position= position+shift_amt
#     new_letter = alphabet[new_position]
#     cipher_text+=new_letter
#   print(f"The encoded word is {cipher_text}")

# # encrypt(plain_txt=text,shift_amt=shift)

# def decrypt(plain_text, shift_amount):
#   txt = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position-shift_amount
#     new_letter = alphabet[new_position]
#     txt+=new_letter

#   print(f"The decoded word is {txt}")

# decrypt(plain_text=text,shift_amount=shift)

# if direction == "encode":
#   encrypt(plain_txt=text,shift_amt=shift)
# elif direction=="decode":
#  decrypt(plain_text=text,shift_amount=shift)


