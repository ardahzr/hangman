import random
import pyfiglet
import time
from colorama import init, Fore, Back, Style
from time import sleep
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
init(autoreset=True)
ascii_banner = pyfiglet.figlet_format("ADAM   ASMACA")
print(Style.BRIGHT + Back.RED + Fore.WHITE + ascii_banner)
kelimeler = "araba uçak kuş elma pizza bilgisayar top kitap kalem defter kedi köpek insan fıstık peynir zeytin gömlek ".split()
foto0 = HANGMAN_PICS[0]
foto1 = HANGMAN_PICS[1]
foto2 = HANGMAN_PICS[2]
foto3 = HANGMAN_PICS[3]
foto4 = HANGMAN_PICS[4]
foto5 = HANGMAN_PICS[5]
foto6 = HANGMAN_PICS[6]
tahmin = 0
kullanilan_harfler = []
kelime = random.choice(kelimeler)
kelime = list(kelime)
ilerleme = len(kelime)
uzunluk = ilerleme * "_ "
def foto_tahmin():
    if tahmin==0:
        print(foto0)
    elif tahmin==1:
        print(foto1)
    elif tahmin==2:
        print(foto2)
    elif tahmin==3:
        print(foto3)
    elif tahmin==4:
        print(foto4)
    elif tahmin==5:
        print(foto5)
    elif tahmin==6:
        print(foto6)
        print("Kaybettin")
        print("Doğru Cevap: " + "".join(kelime))
        ascii_banner2 = pyfiglet.figlet_format("by  Libuntu  &  Mert  Utku  ver:  1.5")
        print(Style.BRIGHT + Back.WHITE + Fore.BLACK + ascii_banner2)
        time.sleep(999999)


print("Harf Sayısı: " + uzunluk)
##########################################################
tahmin1 = input("Harf Tahmin Et: ")
kontrol = 0
bilinmeyen_kelime1 = []
bilinmeyen_kelime2 = []
bilinmeyen_kelime3 = []
bilinmeyen_kelime4 = []
bilinmeyen_kelime5 = []
bilinmeyen_kelime6 = []
bilinmeyen_kelime7 = []
bilinmeyen_kelime8 = []
bilinmeyen_kelime9 = []
bilinmeyen_kelime10 = []
while tahmin1 in kullanilan_harfler:
    print(Style.BRIGHT + Fore.RED + "Bu harfi daha önce kullandınız!")
    tahmin1 = input("Harf Tahmin Et: ")
if tahmin1 in kelime and not kullanilan_harfler:
    print("Kelimedeki Harfler: " + tahmin1)
    print("Doğru Tahmin!")
    foto_tahmin()
    while kontrol < ilerleme:
        if kelime[kontrol]==tahmin1:
            bilinmeyen_kelime1.append(tahmin1 + " ")
        else:
            bilinmeyen_kelime1.append("_ ")
        kontrol += 1
elif tahmin1 not in kelime:
    while kontrol < ilerleme:
        if kelime[kontrol]==tahmin1:
            bilinmeyen_kelime1.append(tahmin1)
        else:
            bilinmeyen_kelime1.append("_ ")
        kontrol += 1
    kullanilan_harfler.append(tahmin1)
    tahmin += 1
    foto_tahmin()
    print("Yanlış Tahmin!!!")
xxx = "".join(bilinmeyen_kelime1)
print(xxx)
print("Yanlış Harfler: " + str(kullanilan_harfler))

if "_ " not in bilinmeyen_kelime1:
    print("Tebrikler Buldunuz!")
    time.sleep(999999)
    
############################################################
kontrol = 0
tahmin2 = input("Harf Tahmin Et: ")
while tahmin2 in kullanilan_harfler:
    print(Style.BRIGHT + Fore.RED + "Bu harfi daha önce kullandınız!")
    tahmin2 = input("Harf Tahmin Et: ")
if tahmin2 in kelime not in kullanilan_harfler:
    print("Kelimedeki Harfler: " + tahmin2)
    print("Doğru Tahmin!")
    foto_tahmin()
    while kontrol < ilerleme:
        if bilinmeyen_kelime1[kontrol]!="_ ":
            bilinmeyen_kelime2.append(bilinmeyen_kelime1[kontrol])
        elif list(kelime)[kontrol]==tahmin2:
            bilinmeyen_kelime2.append(tahmin2 + " ")
        else:
            bilinmeyen_kelime2.append("_ ")
        kontrol += 1

elif tahmin2 not in kelime:
    kullanilan_harfler.append(tahmin2)
    tahmin += 1
    foto_tahmin()
    print("Yanlış Tahmin!!")
    while kontrol < ilerleme:
        if bilinmeyen_kelime1[kontrol]!="_ ":
            bilinmeyen_kelime2.append(bilinmeyen_kelime1[kontrol])
        else:
            bilinmeyen_kelime2.append("_ ")
        kontrol += 1
if "_ " not in bilinmeyen_kelime2:
    print("Tebrikler Buldunuz!")
    time.sleep(999999)
xxx = "".join(bilinmeyen_kelime2)    
print(xxx)
print("Yanlış Harfler: " + str(kullanilan_harfler))

############################################################
kontrol = 0
tahmin3 = input("Harf Tahmin Et: ")
while tahmin3 in kullanilan_harfler:
    print(Style.BRIGHT + Fore.RED + "Bu harfi daha önce kullandınız!")
    tahmin3 = input("Harf Tahmin Et: ")
if tahmin3 in kelime:
    print("Kelimedeki Harfler: " + tahmin3)
    print("Doğru Tahmin!")
    foto_tahmin()
    while kontrol < ilerleme:
        if bilinmeyen_kelime2[kontrol]!="_ ":
            bilinmeyen_kelime3.append(bilinmeyen_kelime2[kontrol])
        elif list(kelime)[kontrol]==tahmin3:
            bilinmeyen_kelime3.append(tahmin3 + " ")
        else:
            bilinmeyen_kelime3.append("_ ")
        kontrol += 1

elif tahmin3 not in kelime:
    kullanilan_harfler.append(tahmin3)
    tahmin += 1
    foto_tahmin()
    print("Yanlış Tahmin!!")
    while kontrol < ilerleme:
        if bilinmeyen_kelime2[kontrol]!="_ ":
            bilinmeyen_kelime3.append(bilinmeyen_kelime2[kontrol])
        else:
            bilinmeyen_kelime3.append("_ ")
        kontrol += 1
if "_ " not in bilinmeyen_kelime3:
    print("Tebrikler Buldunuz!")
    time.sleep(999999)
xxx = "".join(bilinmeyen_kelime3)    
print(xxx)
print("Yanlış Harfler: " + str(kullanilan_harfler))
############################################################
kontrol = 0
tahmin4 = input("Harf Tahmin Et: ")
while tahmin4 in kullanilan_harfler:
    print(Style.BRIGHT + Fore.RED + "Bu harfi daha önce kullandınız!")
    tahmin4 = input("Harf Tahmin Et: ")
if tahmin4 in kelime:
    print("Kelimedeki Harfler: " + tahmin4)
    print("Doğru Tahmin!")
    foto_tahmin()
    while kontrol < ilerleme:
        if bilinmeyen_kelime3[kontrol]!="_ ":
            bilinmeyen_kelime4.append(bilinmeyen_kelime3[kontrol])
        elif list(kelime)[kontrol]==tahmin4:
            bilinmeyen_kelime4.append(tahmin4 + " ")
        else:
            bilinmeyen_kelime4.append("_ ")
        kontrol += 1

elif tahmin4 not in kelime:
    kullanilan_harfler.append(tahmin4)
    tahmin += 1
    foto_tahmin()
    print("Yanlış Tahmin!!")
    while kontrol < ilerleme:
        if bilinmeyen_kelime3[kontrol]!="_ ":
            bilinmeyen_kelime4.append(bilinmeyen_kelime3[kontrol])
        else:
            bilinmeyen_kelime4.append("_ ")
        kontrol += 1
if "_ " not in bilinmeyen_kelime4:
    print("Tebrikler Buldunuz!")
    time.sleep(999999)
xxx = "".join(bilinmeyen_kelime4)    
print(xxx)
print("Yanlış Harfler: " + str(kullanilan_harfler))
############################################################
kontrol = 0
tahmin5 = input("Harf Tahmin Et: ")
while tahmin5 in kullanilan_harfler:
    print(Style.BRIGHT + Fore.RED + "Bu harfi daha önce kullandınız!")
    tahmin5 = input("Harf Tahmin Et: ")
if tahmin5 in kelime:
    print("Kelimedeki Harfler: " + tahmin5)
    print("Doğru Tahmin!")
    foto_tahmin()
    while kontrol < ilerleme:
        if bilinmeyen_kelime4[kontrol]!="_ ":
            bilinmeyen_kelime5.append(bilinmeyen_kelime4[kontrol])
        elif list(kelime)[kontrol]==tahmin5:
            bilinmeyen_kelime5.append(tahmin5 + " ")
        else:
            bilinmeyen_kelime5.append("_ ")
        kontrol += 1

elif tahmin5 not in kelime:
    kullanilan_harfler.append(tahmin5)
    tahmin += 1
    foto_tahmin()
    print("Yanlış Tahmin!!")
    while kontrol < ilerleme:
        if bilinmeyen_kelime4[kontrol]!="_ ":
            bilinmeyen_kelime5.append(bilinmeyen_kelime4[kontrol])
        else:
            bilinmeyen_kelime5.append("_ ")
        kontrol += 1
if "_ " not in bilinmeyen_kelime5:
    print("Tebrikler Buldunuz!")
    time.sleep(999999)
xxx = "".join(bilinmeyen_kelime5)    
print(xxx)
print("Yanlış Harfler: " + str(kullanilan_harfler))

############################################################
kontrol = 0
tahmin6 = input("Harf Tahmin Et: ")
while tahmin6 in kullanilan_harfler:
    print(Style.BRIGHT + Fore.RED + "Bu harfi daha önce kullandınız!")
    tahmin6 = input("Harf Tahmin Et: ")
if tahmin6 in kelime:
    print("Kelimedeki Harfler: " + tahmin6)
    print("Doğru Tahmin!")
    foto_tahmin()
    while kontrol < ilerleme:
        if bilinmeyen_kelime5[kontrol]!="_ ":
            bilinmeyen_kelime6.append(bilinmeyen_kelime5[kontrol])
        elif list(kelime)[kontrol]==tahmin6:
            bilinmeyen_kelime6.append(tahmin6 + " ")
        else:
            bilinmeyen_kelime6.append("_ ")
        kontrol += 1

elif tahmin6 not in kelime:
    kullanilan_harfler.append(tahmin6)
    tahmin += 1
    foto_tahmin()
    print("Yanlış Tahmin!!")
    while kontrol < ilerleme:
        if bilinmeyen_kelime5[kontrol]!="_ ":
            bilinmeyen_kelime6.append(bilinmeyen_kelime5[kontrol])
        else:
            bilinmeyen_kelime6.append("_ ")
        kontrol += 1
if "_ " not in bilinmeyen_kelime6:
    print("Tebrikler Buldunuz!")
    time.sleep(999999)
xxx = "".join(bilinmeyen_kelime6)    
print(xxx)
print("Yanlış Harfler: " + str(kullanilan_harfler))
############################################################
kontrol = 0
tahmin7 = input("Harf Tahmin Et: ")
while tahmin7 in kullanilan_harfler:
    print(Style.BRIGHT + Fore.RED + "Bu harfi daha önce kullandınız!")
    tahmin7 = input("Harf Tahmin Et: ")
if tahmin7 in kelime:
    print("Kelimedeki Harfler: " + tahmin7)
    print("Doğru Tahmin!")
    foto_tahmin()
    while kontrol < ilerleme:
        if bilinmeyen_kelime6[kontrol]!="_ ":
            bilinmeyen_kelime7.append(bilinmeyen_kelime6[kontrol])
        elif list(kelime)[kontrol]==tahmin7:
            bilinmeyen_kelime6.append(tahmin7 + " ")
        else:
            bilinmeyen_kelime6.append("_ ")
        kontrol += 1

elif tahmin7 not in kelime:
    kullanilan_harfler.append(tahmin7)
    tahmin += 1
    foto_tahmin()
    print("Yanlış Tahmin!!")
    while kontrol < ilerleme:
        if bilinmeyen_kelime6[kontrol]!="_ ":
            bilinmeyen_kelime7.append(bilinmeyen_kelime6[kontrol])
        else:
            bilinmeyen_kelime7.append("_ ")
        kontrol += 1
if "_ " not in bilinmeyen_kelime7:
    print("Tebrikler Buldunuz!")
    time.sleep(999999)
xxx = "".join(bilinmeyen_kelime7)    
print(xxx)
print("Yanlış Harfler: " + str(kullanilan_harfler))
############################################################
kontrol = 0
tahmin8 = input("Harf Tahmin Et: ")
while tahmin8 in kullanilan_harfler:
    print(Style.BRIGHT + Fore.RED + "Bu harfi daha önce kullandınız!")
    tahmin8 = input("Harf Tahmin Et: ")
if tahmin8 in kelime:
    print("Kelimedeki Harfler: " + tahmin8)
    print("Doğru Tahmin!")
    foto_tahmin()
    while kontrol < ilerleme:
        if bilinmeyen_kelime7[kontrol]!="_ ":
            bilinmeyen_kelime8.append(bilinmeyen_kelime7[kontrol])
        elif list(kelime)[kontrol]==tahmin8:
            bilinmeyen_kelime7.append(tahmin8 + " ")
        else:
            bilinmeyen_kelime7.append("_ ")
        kontrol += 1

elif tahmin8 not in kelime:
    kullanilan_harfler.append(tahmin8)
    tahmin += 1
    foto_tahmin()
    print("Yanlış Tahmin!!")
    while kontrol < ilerleme:
        if bilinmeyen_kelime7[kontrol]!="_ ":
            bilinmeyen_kelime8.append(bilinmeyen_kelime7[kontrol])
        else:
            bilinmeyen_kelime8.append("_ ")
        kontrol += 1
if "_ " not in bilinmeyen_kelime8:
    print("Tebrikler Buldunuz!")
    time.sleep(999999)
xxx = "".join(bilinmeyen_kelime8)    
print(xxx)
print("Yanlış Harfler: " + str(kullanilan_harfler))
############################################################
kontrol = 0
tahmin9 = input("Harf Tahmin Et: ")
while tahmin9 in kullanilan_harfler:
    print(Style.BRIGHT + Fore.RED + "Bu harfi daha önce kullandınız!")
    tahmin9 = input("Harf Tahmin Et: ")
if tahmin9 in kelime:
    print("Kelimedeki Harfler: " + tahmin9)
    print("Doğru Tahmin!")
    foto_tahmin()
    while kontrol < ilerleme:
        if bilinmeyen_kelime8[kontrol]!="_ ":
            bilinmeyen_kelime9.append(bilinmeyen_kelime8[kontrol])
        elif list(kelime)[kontrol]==tahmin8:
            bilinmeyen_kelime8.append(tahmin9 + " ")
        else:
            bilinmeyen_kelime8.append("_ ")
        kontrol += 1

elif tahmin9 not in kelime:
    kullanilan_harfler.append(tahmin9)
    tahmin += 1
    foto_tahmin()
    print("Yanlış Tahmin!!")
    while kontrol < ilerleme:
        if bilinmeyen_kelime8[kontrol]!="_ ":
            bilinmeyen_kelime9.append(bilinmeyen_kelime8[kontrol])
        else:
            bilinmeyen_kelime9.append("_ ")
        kontrol += 1
if "_ " not in bilinmeyen_kelime9:
    print("Tebrikler Buldunuz!")
    time.sleep(999999)
xxx = "".join(bilinmeyen_kelime9)    
print(xxx)
print("Yanlış Harfler: " + str(kullanilan_harfler))
############################################################
kontrol = 0
tahmin10 = input("Harf Tahmin Et: ")
while tahmin10 in kullanilan_harfler:
    print(Style.BRIGHT + Fore.RED + "Bu harfi daha önce kullandınız!")
    tahmin10 = input("Harf Tahmin Et: ")
if tahmin10 in kelime:
    print("Kelimedeki Harfler: " + tahmin10)
    print("Doğru Tahmin!")
    foto_tahmin()
    while kontrol < ilerleme:
        if bilinmeyen_kelime9[kontrol]!="_ ":
            bilinmeyen_kelime10.append(bilinmeyen_kelime9[kontrol])
        elif list(kelime)[kontrol]==tahmin9:
            bilinmeyen_kelime9.append(tahmin10 + " ")
        else:
            bilinmeyen_kelime9.append("_ ")
        kontrol += 1

elif tahmin10 not in kelime:
    kullanilan_harfler.append(tahmin10)
    tahmin += 1
    foto_tahmin()
    print("Yanlış Tahmin!!")
    while kontrol < ilerleme:
        if bilinmeyen_kelime9[kontrol]!="_ ":
            bilinmeyen_kelime10.append(bilinmeyen_kelime9[kontrol])
        else:
            bilinmeyen_kelime10.append("_ ")
        kontrol += 1
if "_ " not in bilinmeyen_kelime10:
    print("Tebrikler Buldunuz!")
    time.sleep(999999)
xxx = "".join(bilinmeyen_kelime10)    
print(xxx)
print("Yanlış Harfler: " + str(kullanilan_harfler))
print("Bu kadar da bilemediysen sie")




