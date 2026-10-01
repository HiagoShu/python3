#TRATAMENTO DE ERROS E EXCEÇÕES

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
# except Exception as erro:
#     print(f'Problema encontrado: {erro.__class__.__name__}')
except (ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt: #Se apertar ctrl+c, o programa não quebra, ele entra nesse except
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')