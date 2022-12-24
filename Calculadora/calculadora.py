


def soma(values):
    result = 0
    for value in values:
        result += value 
    return f"The result is {result}"


def subitracao(values):
    result = values[0]
    values.pop(0)
    for value in values:
        result -= value 
    return f"The result is {result}"


def divisao(value1, value2):
    result = value1 / value2
    return f"The result is {result}"


def multiplicacao(values):
    result = values[0]
    values.pop(0)
    for value in values:
        result *= value 
    return f"The result is {result}"


def exponenciacao(value1, value2):    
    result = value1 ** value2 
    return f"The result is {result}"







