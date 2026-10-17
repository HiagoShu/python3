from poligono import Quadrado,Circulo

def main():
    q = Quadrado(2)

    print(f"Perímetro Quadrado = {q.perimetro():.1f} cm")
    print(f"Área Quadrado = {q.area():.1f} cm²")

    c = Circulo(20)
    print(f"Perímetro Círculo = {c.perimetro():.1f} cm")
    print(f"Área Círculo = {c.area():.1f} cm²")

    

if __name__ == "__main__":
    main()