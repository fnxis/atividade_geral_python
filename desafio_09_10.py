import random
soma=0
media=0
Lista=[random.randint(1,100)for _ in range(5)]

def main():
    def adicionarLista(lista):
        lista.append()
        return lista

    def removerLista(lista):
        lista.remove()
        return lista

    def exibirListaAtual(lista):
        return lista

    def calcularLista(soma):
        for numero in Lista:
            soma=soma+numero
        return soma

    def mediaLista(lista):
        media=sum(lista)/len(lista)
        return media

    while True:
        try:
            digito=int(input("Digite 1 para adicionar um numero a lista\nDigite 2 para remover um numero da lista\nDigite 3 para exibir a lista\nDigite 4 para somar a lista\nDigite 5 para saber a media da lista\ndigite 6 para sair\n:"))
            if digito == 1:
                add=input(int("digite um numero para adicionar")) 
                print(adicionarLista(add))
            if digito == 2:
                rm=input(int("digite um numero para remover"))
                print(removerLista(rm))
            if digito == 3:
                print(exibirListaAtual(Lista))
            if digito == 4:
                print(calcularLista(soma))
            if digito == 5: 
                print(mediaLista(Lista))    
            if digito == 6:
                print("Encerrando processo.")
                break    
            else:
                print("Digite um numero valido")   
              
main()