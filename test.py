import os

def erase():  # Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    if os.name == 'nt': #linux
        os.system('cls')
    elif os.name == 'posix': #windows
        os.system('clear')

senha=input("Escreva uma mensagem:")
cod=""
for i in senha:
    cod = cod + chr(ord(i)+10)
print(cod)
decod = cod - chr(ord(i)+10)   
print(decod)