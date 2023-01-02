import os
from time import sleep


carros = [
        ("Chevrolet Tracker", 120), 
        ("Chevrolet Onix", 90), 
        ("Chevrolet Spin", 150),
        ("Hyundai HB20", 85), 
        ("Hyundai Tucson", 120), 
        ("Fiat Uno", 60), 
        ("Fiat Mobi", 70), 
        ("Fiat Pulse", 130)
        ]

alugados = []


def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia.".format(i, car[0], car[1]))
        
def schema_inicial():
    print("===============================")
    print("Bem vindo à locadora de carros!")
    print("===============================")
    print("O que deseja fazer?")
    print("0 - Mostrar portifólio")
    print("1 - Alugar um carro")
    print("2 - Devolver um carro")    
    option = int(input())
    return option

def action_validator(action):
    if not 0 <= action <= 2:
        print("Entrada inválida, por favor colocar uma das opções disponíveis")
        sleep(2)
        main()

def main():
    os.system("clear")
    action = schema_inicial()
    
    action_validator(action)
    
    os.system("clear")
    if action == 0:
        mostrar_lista_de_carros(carros)

    elif action == 1:
        mostrar_lista_de_carros(carros)
        print("===============================")
        print("Escolha o código do carro:")
        cod_car = int(input())
        
        if cod_car not in enumerate(carros):
            print('Código indisponíve, por favor informar o código correto \n')
            sleep(2)
            main()
        
        print("Por quantos dias você deseja alugar este carro?")
        dias = int(input())
        os.system("clear")

        print(f"Você escolheu {carros[cod_car][0]} por {dias} dias.")
        print(f"O aluguel totalizaria R$ {dias * carros[cod_car][1]}. Deseja alugar?")
        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
            print(f"Parabéns você alugou o {carros[cod_car][0]} por {dias} dias.")
            alugados.append(carros.pop(cod_car))

    elif action == 2:
        if len(alugados) == 0:
            print("Não há carros para devolver.")
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            mostrar_lista_de_carros(alugados)
            print("\n Escolha o código do carro que deseja devolver:")
            cod = int(input())
            
            print("Desenja devolver o carro? ")
            print("0 - SIM | 1 - NÃO")
            conf = int(input())
            if conf == 0:
                print(f"Obrigado por devolver o carro {alugados[cod][0]} \n")
                carros.append(alugados.pop(cod))
    
    print("===============================")
    print("0 para CONTINUAR")
    print("1 para SAIR")
    if float(input()) == 0:
        main()
    
if __name__ == "__main__":
    main()
    