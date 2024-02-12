""""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse
ângulo"""

from math import sin, cos, tan, radians


angulo = float(input("Digite o valor do angulo: "))

seno = sin(radians(angulo))
print('O valor do seno é {:.2f}'. format(seno))

cosseno = cos(radians(angulo))
print('O valor do cosseno é {:.2f}'.format(cosseno))

tangente = tan(radians(angulo))
print('O valor da tangente é {:.2f}'.format(tangente))