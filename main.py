import random

lowers= "abcdefghijklmnopqrstuvxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
numbers= "1234567890"

extension = int(input("longitud de la contraseña:  "))

string = lowers + uppers + numbers

password = "".join(random.sample(string,extension))

print(password)