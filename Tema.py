#Um navio cargueiro radioativo naufragou na costa e temos que criar um programa de criptografia para enviar uma mensagem sobre a situação atual.

#Temos que fazer um progama que traduza as mensagens nesta situação específicas.
senha=input("escreva uma mensagem")
box=[]
cod=""
recor=""
o=0
for i in senha:
    #cod= cod + chr(ord(i)+5)
    print(o)
    box.insert(o,ord(i))
    print(box[o])
    o = o+1
    #for i in cod:
    #recor=recor + chr(ord(i)-5)
print(cod)
print(recor)