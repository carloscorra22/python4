class veiculo():
    def color( Color):
        return Color

    def ruedas(numero):
        return numero

    def puertas(cantidad):
        return cantidad

class coche(veiculo):

    def velocidad(Velocidad):
        return Velocidad

    def cilindrada(cilindros):
        return cilindros


Coche= coche()

print(coche.color("azul"))

print(coche.cilindrada(5))

print(coche.velocidad(120))