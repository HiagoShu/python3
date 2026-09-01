frase = 'Curso em Video Python'
#Fatiamento
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Análise
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

#Transformação
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

# Remoção
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

# Divisão
print(frase.split())

# Junção 
'-'.join(frase)
print(frase)