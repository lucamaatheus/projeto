lista=[]
for i in range(3):
   convidados=str(input("digite o nome dos convidados: "))
   lista+=[convidados]
tirar=str(input("digite o convidado que desistiu: "))
lista.remove(tirar)
print("lista final",lista)

               
 