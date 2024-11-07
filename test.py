import os
import time

#Temos que fazer um progama que traduza as mensagens nesta situação específicas.

def erase():  # Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    if os.name == 'nt': #linux
        os.system('cls')
    elif os.name == 'posix': #windows
        os.system('clear')

senha=input("escreva uma mensagem: ")
cod2=[]
cod=""
recor=""
for i in senha:
    cod= cod + chr(ord(i)+10)
for i in cod:
    recor=recor + chr(ord(i)-10)
print(cod)
print(recor)

