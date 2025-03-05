
def divisao():
    try:
        numero1=int(input("qual o primeiro numero da divisao?"))
        numero2=int(input("qual o segundo numero da divisao?"))
        divi=numero1/numero2
        return divi
    except ValueError:
        return"digite um numero inteiro"
    except ZeroDivisionError:
        return"nao é possivel dividir por 0"

resultado=divisao()
print(resultado)
