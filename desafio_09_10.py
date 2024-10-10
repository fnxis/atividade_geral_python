import random
soma=0
media=0
add=None
Lista=[random.randint(1,100)for _ in range(5)]

def main():
    def adicionarLista(lista):
        lista.append(add)
        return lista

    def removerLista(lista):
        lista.remove(rm)
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
                print(adicionarLista(Lista))
            elif digito == 2:
                rm=input("digite um numero para remover")
                print(removerLista(Lista))
            elif digito == 3:
                print(exibirListaAtual(Lista))
            elif digito == 4:
                print(calcularLista(soma))
            elif digito == 5: 
                print(mediaLista(Lista))    
            elif digito == 6:
                print("Encerrando processo.")
                break    
            else:
                print("Digite um numero valido")   
        except Exception:
            print("é isso")      
main()