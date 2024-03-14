def celsius_to_fahrenheit(Celsius):
    return (Celsius * 9/5) + 32
def fahrenheit_to_celsius(Fahrenheit):
    return (Fahrenheit - 32) * 5/9
def celsius_to_kelvin(Celsius):
    return Celsius + 273.15
def kelvin_to_celsius(Kelvin):
    return Kelvin - 273.15
def celsius_to_rankine(Celsius):
    return (Celsius + 273.15) * 9/5
def rankine_to_celsius (Rankine):
    return (Rankine - 491.67) * 5/9
def fahrenheit_to_kelvin(Fahrenheit):
    return (Fahrenheit + 459.67) * 5/9
def fahrenheit_to_rankine(Fahrenheit):
    return Rankine + 459.67
def kelvin_to_fahrenheit(Kelvin):
    return 1.8 * (Kelvin - 273) + 32
def kelvin_to_rankine(Kelvin):
    return Kelvin * 1.8
def rankine_to_fahrenheit(Rankine):
    return Rankine - 459.67
def rankine_to_kelvin(Rankine):
    return Rankine/1.8



print('Obrigada por escolher este programa de conversão de temperatura <3\n')


def main():
    print('Em que unidade a temperatura inicial?')
    print('1 - Celsius')
    print('2 - Fahrenheit')
    print('3 - Kelvin')
    print('4 - Rankine')
    inicial = int(input('Digite o número de sua escolha:\n'))

    temperatura = float(input('Digite a temperatura que você quer converter:\n'))

    print('\nEm qual unidade deseja converter?')
    print('1 - Celsius')
    print('2 - Fahrenheit')
    print('3 - Kelvin')
    print('4 - Rankine')
    desejada=int(input('Digite o número de sua escolha:\n'))

    if inicial == 1: #celsius
        if desejada == 1:
            print('Mor, a temperatura inicial e a desejada são as mesma veyr')
        elif desejada == 2:
            print('Temperatura em Fahrenheit:', celsius_to_fahrenheit(temperatura))
        elif desejada == 3:
            print('Temperatura em Kelvin:', celsius_to_kelvin(temperatura))
        elif desejada == 4:
            print('Temperatura em Rankine:', celsius_to_kelvin(temperatura))
        else:
            print('Mor, deu de antisse, não tem essa opção 0^0')

    elif inicial == 2: #fahrenheit
        if desejada == 2:
            print('Mor, a temperatura inicial e a desejada são as mesmas veyr')
        elif desejada == 1:
            print('Temperatura em Celsius:', fahrenheit_to_celsius(temperatura))
        elif desejada == 3:
            print('Temperatura em Kelvin:', fahrenheit_to_kelvin(temperatura))
        elif desejada == 4:
            print('Temperatura em Rankine:',fahrenheit_to_rankine(temperatura))

    elif inicial == 3: #kelvin
        if desejada == 3:
            print('Mor, a temperatura inicial e a desejada são as mesmas veyr')
        elif desejada == 1:
            print('Temperatura em Celsius:', kelvin_to_celsius(temperatura))
        elif desejada == 2:
            print('Temperatura em Fahrenheit:', kelvin_to_fahrenheit(temperatura))
        elif desejada == 4:
            print('Temperatura em Rankine:', kelvin_to_rankine(temperatura))

    elif inicial == 4:  #rankine
        if desejada == 4:
            print('Mor, a temperatura inicial e a desejada são as mesmas veyr')
        elif desejada == 1:
            print('Temperatura em Celsius:', rankine_to_celsius(temperatura))
        elif desejada == 2:
            print('Temperatura em Fahrenheit:', rankine_to_fahrenheit(temperatura))
        elif desejada == 3:
            print('Temperatura em Kelvin:', rankine_to_kelvin(temperatura))

if __name__=='__main__':
    main()


print('\nTchau mor, volte sempre <3')



