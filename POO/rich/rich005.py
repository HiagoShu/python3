from rich.traceback import install
install()


def divisao(x,y):
    return x/y 

# divisao(10,2)

#Versão de erro com install() do rich.traceback
divisao(50,0)