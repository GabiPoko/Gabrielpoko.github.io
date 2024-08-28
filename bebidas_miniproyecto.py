
# Intente crear una instancia de clase con los atributos bebida, precio e ingredientes
# se puede crear tantos objetos como bebidas haya en el menu y despues agregar mas


class BebidasMenu:

    def __init__(self, bebida, precio, ingredientes):
        self.bebida = bebida
        self.precio = precio
        self.ingredientes = ingredientes

    def mostrar_bebida(self):
        print (f'*' * 5, self.bebida.upper(),'*'* 5)
        print (f' {self.bebida}: {self.precio}\n Ingredientes: {self.ingredientes}')

campari = BebidasMenu('Campari', 3500, 'Naranja, aguardiente y jarabe azucarado')
martini = BebidasMenu('Martini', 3000, 'ginebra y vermú')
manhattan = BebidasMenu('Manhattan', 4000, 'Whisky con martini rojo')
limonada = BebidasMenu('Limonada', 2500, 'Limon, azucar y agua')
licuado = BebidasMenu('Licuado', 3000, 'Zumo de Fruta y agua')
mojito = BebidasMenu ('Mojito', 2000, 'Lima, menta y azucar')

martini.mostrar_bebida()


    