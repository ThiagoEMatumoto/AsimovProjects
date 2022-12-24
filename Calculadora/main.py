from calculadora import *
import os

def main():
    while True:
        os.system("clear")

        operators = { "+" : "mais",
                    "-" : "menos",
                    "%" : "divisao",
                    "*" : "multiplicacao",
                    "^" : "exponensiacao"
                    }
        
        operator = None
        
        while operator not in operators:
            print(f'What do you want to do:')
            for operator in operators:
                print(f'{operator} : {operators[operator]} ')
            try:
                operator = input("\n")
            except:
                print("Value isn't valid")
        
        if operator != "^" and operator != "%":
            values = []
            while True:
                try:
                    values.append(int(input('Inform a value: ')))
                except:
                    print('Please, put a number')
                    continue
                can_I_continue =int(input("do you want to add one more value [0-No][1-Yes]?\n"))
                if not can_I_continue:
                    if operator == "+":
                        print(soma(values))
                        break
                    elif operator == '-':
                        print(subitracao(values))
                        break
                    elif operator == "*":
                        print(multiplicacao(values))
                        break
        else:
            try:
                value1 = int(input('Inform the first value: '))
                value2 = int(input('Inform the second value: '))
            except:
                print('Please, put a number')
                continue
            if operator == '%':
                print(divisao(value1, value2))
            else:
                print(exponenciacao(value1, value2))  
        can_I_continue =int(input("you want to perform another calculation [0-No][1-Yes]? \n"))
        if not can_I_continue:
            break

if __name__ == "__main__":
    main()
