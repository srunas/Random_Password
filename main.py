import random

chars = "+-/*!&$#@?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lenght = int( input( "Длина строки: " ) )

password = ""

for i in range( lenght ):
    password += random.choice( chars )

key = int(input("Введите ключ шифрования диапазоном 1-76: "))
wordX = ""

for i in password:
    position = password.find(i)
    newPosition = position + key
    if i in password:
        wordX = wordX + chars[newPosition]
    else:
        wordX = wordX + i

print( password )

file = open( 'password.txt', 'a')
file.write( password )
