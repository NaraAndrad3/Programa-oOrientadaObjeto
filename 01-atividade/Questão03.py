forma = str(input('Digite a forma(quadrado, triângulo ou circulo):\n'))
area = 0
pi = 3.14
if forma == 'quadrado' or forma == 'Quadrado':
    print('Você escolheu: Quadrado')
    lado = float(input('Digite o tamanho do lado do quadrado:\n'))
    area = lado ** 2
    print('A área do quadrado é: {}'.format(area))
elif forma == 'triangulo' or forma == 'triâgulo' or forma == 'Triangulo' or forma == 'Triângulo':
    print('Você escolheu triângulo ')
    base = float(input('Digite o valor da base\n'))
    altura = float(input('Digite o valor da altura\n'))
    area = (base*altura)/2
    print('A área do triangulo é: {}'.format(area))
elif forma =='circulo' or forma =='Circulo' or forma == 'círculo' or forma == 'Círculo':
    print('Você escolheu circulo')
    raio = float(input('Digite o valor do raio\n'))
    area = pi*(raio**2)
    print('A área do circulo é: {}'.format(area))
else:
    print('Digite uma opção válida')


