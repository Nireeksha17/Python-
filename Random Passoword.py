import random
passlen = int(input("Enter the length of your password"))
characters_of_password ="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(characters_of_password,passlen))
print(p)
