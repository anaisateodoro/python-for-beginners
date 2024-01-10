import random

numero_aleatorio = random.randint(0, 100)
numero = int(input('Ingresa un número para comenzar: '))
intentos = 0
cantidad_pistas = 2
cantidad_intentos = 2

while numero != numero_aleatorio:
    print('Vaya, lo siento, ¡no lograste adivinar el número!')
    intentos += 1

    if intentos >= cantidad_intentos:
        if cantidad_pistas > 0:
            pista = input('¿Te gustaría recibir una pista? (si/no) ')

            if pista == 'si':
                if numero < numero_aleatorio:
                    print(f'Aquí tienes tu pista: Tu número {numero =} es menor.')
                else:
                    print(f'Aquí tienes tu pista: Tu número {numero =} es mayor.')
                cantidad_pistas -= 1
            else:
                pista = input('Te quedaste sin pistas. ¿Quieres seguir jugando? (si/no) ')

                if pista == 'no':
                    print('¡Te rendiste, cobarde!')
                    break

    numero = int(input('Inténtalo de nuevo con otro número: '))
else:
    print('¡Excelente! Lo lograste, has adivinado el número.')
