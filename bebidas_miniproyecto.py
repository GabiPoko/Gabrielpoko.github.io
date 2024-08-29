
# Intente crear una instancia de clase con los atributos bebida, precio e ingredientes
# se puede crear tantos objetos como bebidas haya en el menu y despues agregar mas


# class BebidasMenu:

#     def __init__(self, bebida, precio, ingredientes):
#         self.bebida = bebida
#         self.precio = precio
#         self.ingredientes = ingredientes

#     def mostrar_bebida(self):
#         print (f'*' * 5, self.bebida.upper(),'*'* 5)
#         print (f' {self.bebida}: {self.precio}\n Ingredientes: {self.ingredientes}')

# campari = BebidasMenu('Campari', 3500, 'Naranja, aguardiente y jarabe azucarado')
# martini = BebidasMenu('Martini', 3000, 'ginebra y vermú')
# manhattan = BebidasMenu('Manhattan', 4000, 'Whisky con martini rojo')
# limonada = BebidasMenu('Limonada', 2500, 'Limon, azucar y agua')
# licuado = BebidasMenu('Licuado', 3000, 'Zumo de Fruta y agua')
# mojito = BebidasMenu ('Mojito', 2000, 'Lima, menta y azucar')

# martini.mostrar_bebida()

menus=[
{
    "tipo": "casero",
    "nombre":"Pasta al pesto",
    "precio":8000
},
{
    "tipo": "casero",
    "nombre":"Ensalada César",
    "precio":6500
},
{
    "tipo": "casero",
    "nombre":"Tacos al pastor",
    "precio":8500
},
{
    "tipo": "gourmet",
    "nombre":"Foie Gras a la plancha con reducción de oporto y chutney de higos",
    "precio":35000
},
{
    "tipo": "gourmet",
    "nombre":"Ossobuco a la milanesa con risotto de azafrán",
    "precio":25000
},
{
    "tipo": "gourmet",
    "nombre":"Langosta thermidor con salsa de mantequilla y brandy",
    "precio":55000
},
{
    "tipo": "vegano",
    "nombre":"Lentejas estofadas con verduras",
    "precio":7500
},
{
    "tipo": "vegano",
    "nombre":"Burrito de frijoles negros",
    "precio":6000
},
{
    "tipo": "vegano",
    "nombre":"Pasta con pesto de espinacas",
    "precio":7800
}
]

print (menus)

    