import os 
import sys 
import random
import string

all_chars = string.ascii_letters + string.digits + string.punctuation + " "

all_chars = list(all_chars)

kay = all_chars.copy()
random.shuffle(kay)

menu = """
Choose
1) Show the map
2) Encryption the message
3) Dencryption the message
4) to exti the program
"""

def st():
    def show():
        print(kay)
        var = input("do you want to run again? ")
        if var.lower()=='no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower()=='yes':
            st()

    def Encryption():
        plain_text = input("enter your message to encrypt: ")
        cipher_text = ""
        for letter in plain_text:
            index = all_chars.index(letter)
            cipher_text += kay[index]
        print(f"Encryption Message: {cipher_text}")
        var = input("do you want to run again? ")
        if var.lower()=='no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower()=='yes':
            st()

    def Dencryption():
        cipher_text = input("enter your message to dencrypt: ")
        plain_text = ""
        for letter in cipher_text:
            index = kay.index(letter)
            plain_text += all_chars[index]
        print(f"Dencryption Message: {plain_text}")
        var = input("do you want to run again? ")
        if var.lower()=='no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower()=='yes':
            st()

    def exit():
        print("good bye")
        os.execl(sys.executable, sys.executable, *sys.argv)

    ans = input(menu)
    if ans =='1':
        show()
    if ans=='2':
        Encryption()
    if ans=='3':
        Dencryption()
    if ans=='4':
        exit()
st()