def verificar_compra(dinheiro,custo):
    
    if dinheiro >=custo:
        print("compra bem sucedida")
    else:
        falta=custo-dinheiro
        print( "alerta:dinheiro insuficiente, falta R$", falta, "para completar")
dinheiro= float(input("digite o valor que voce tem: "))
custo= float(input("digite o valor gasto: "))
print(verificar_compra(dinheiro,custo))