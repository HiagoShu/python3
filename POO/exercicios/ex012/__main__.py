from classes import *
def main():
    a = Cachorro("Bandito")
    b = Gato("Mingau")
    c = Pato("Donald")
    d = Galinha("Clara")
    a.emitir_som()
    b.emitir_som()
    c.emitir_som()
    d.emitir_som()


    e = Spitz("Destruidora de Mundos")
    f = Pitbull("Luluzinha")
    e.emitir_som()
    f.emitir_som()
if __name__ == "__main__":
    main()