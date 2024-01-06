#Sucessor e antecedor de um número

#Jeito 1 - Primeira forma
n = int(input('Digite um número: '))
a = n-1
s = n+1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n,a,s))

#Jeito 2 - Outra forma de inserir o desafio
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é{}'.format(n,(n-1),(n+1)))

#Jeito 2 - Outra forma de inserir o desafio
n=int(input('Digite um número: '))
print('Analisando o seu número ')
print(f'Seu antecessor é {n-1} e seu sucessor é {n+1}!')

# Jeito 3 - Outra forma de inserir o desafio
while True:
   try:
       n = int(input('Digite um número: '))
       print('Analisando o seu número ')
       print(f'Seu antecessor é {n-1} e seu sucessor é {n+1}!')
       break
   except ValueError:
       print('Por favor, digite um número válido!')
