"""
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
"""

# Alguns exemplos de Palíndromo
'''
La vou eu em meu eu oval
Luz azul
Mega bobagem
Me ve se a panela da moça e de aço Madalena Paes e vem
Missa é assim
O ceu sueco
O galo ama o lago
Ola galo
Ole Maracuja caju caramelo
O lobo ama o bolo
O romano acata amores a damas amadas e Roma ataca o namoro
O teu dueto
otimo só eu que os omito
O trote torto
Rir o breve verbo rir
Roma é amor
Roma me tem amor
Saíram o tio e oito Marias
Seco de raiva coloco no colo caviar e doces
Socorram-me subi no ônibus em Marrocos


Ada
Ana
Hanah
Maram
Nahan
Natan
Oto
Reinier
Renner
'''


print()

termo = input('Digite uma palavra ou frase: ')

termo = termo.upper()
termo_inverso = termo[::-1]
termo_sem_espaco = termo.replace(' ', '')
termo_sem_espaco_inverso = termo_inverso.replace(' ', '')
print('\n' * 1)
print(f'Termo digitado: {termo}')
print(f'\nTermo inverso:  {termo_inverso}')

if termo_sem_espaco == termo_sem_espaco_inverso:
    print('\nO termo digitado é um Palíndrono.\n')
else:
    print('\nO termo digitado não é um Palídrono.\n')