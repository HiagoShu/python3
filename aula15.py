# Como interromper um código.
# Exemplo: No código abaixo, se percebe que o flag é adicionado junto a contagem de números, sem ser possível tirá-lo da contagem sem uma gambiarra.

#n = s = 0
#while n!= 999:
#    n = int(input('Digite um número: '))
#    s+=n 
#s -= 999
#print('A soma vale {}'.format(s))


#Agora veremos a forma sem gambiarra. 

#n = s = 0
#while True: #Roda infinitamente
#    n = int(input('Digite um número: '))
#    if n == 999:
#        break  #Numa condição, ou seja, se o usuário selecionar o flag, o while é quebrado/ terminado.
#    s += n 
#print('A soma vale {}'.format(s))

#f strings
#Interpolação dentro de strings
#print(f'A soma vale {s}')

#Mais exemplos com f strings
nome = 'José'
idade = 33 
salário = 987.3
print(f'Oi, meu nome é {nome}, e tenho {idade} anos, e ganho R${salário:.2f}')