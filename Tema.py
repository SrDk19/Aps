#Um navio cargueiro radioativo naufragou na costa e temos que criar um programa de criptografia para enviar uma mensagem sobre a situação atual.

#Temos que fazer um progama que traduza as mensagens nesta situação específicas.
senha=input("escreva uma mensagem")
cod=""
for i in senha:
    cod= cod + chr(ord(i)+10)
print(cod)