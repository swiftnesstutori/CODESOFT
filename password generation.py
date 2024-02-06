#password generation
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("Welcome to the Password Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
password_list = []
for char in range(num_letters):
    password_list.append(random.choice(letters))
for char in range(num_symbols):
    password_list += random.choice(symbols)
for char in range(num_numbers):
    password_list += random.choice(numbers)
random.shuffle(password_list)
password = ''.join(password_list)
print(f"Your Password is : {password}")