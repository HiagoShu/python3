#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite aqui o preço do produto: R$'))

des= preco * 0.95

print('O preço do produto é R${:.2f}, e o preço com desconto é de R${:.2f}'.format(preco,des))
