
# Intendando crear un menú con una clase Menu_bebida

# class MenuAlcohol:
#     def __init__(self):
#         self.menu = {'Campari': [3000, ['naranja amarga, aguardiente y jarabe azucarado']],
#                     'Martini': [2500, ['ginebra y vermú']], 'Margarita': [3000, ['tequila blanco, jugo de limón y licor de naranja']], 
#                     'Manhattan': [3500, ['Whisky con martini rojo']], 'Fernet': [2000, ['Fernet branca con gaseosa cola']]}
 
#     def menu_mostrar (self):
#         print ('MENU BEBIDAS')
#         for bebida, info in self.menu.items():
#            precio, ingredientes = info
#            print(f'{bebida}: ${precio}')
#            print(f'Ingredientes: {', '.join(ingredientes)}')
#            print("-" * 30)

# menu = MenuAlcohol()
# menu.menu_mostrar ()


# menu_bebidas = [{'tipo': 'Sin alcohol'}, ]


# martini.mostrar_bebida()

menu_bebida =[
{
    "tipo": "Con alcohol",
    "nombre":"Campari: naranja amarga, aguardiente y jarabe azucarado",
    "precio": 3000
},
{
    "tipo": "Con alcohol",
    "nombre":"Martini",
    "precio": 2500
},
{
    "tipo": "Con alcohol",
    "nombre":"Ginebra y vermú",
    "precio": 3500
},
{
    "tipo": "Sin alcohol",
    "nombre":"Limonada: Limón, azucar y agua",
    "precio": 3000
},
{
    "tipo": "Sin alcohol",
    "nombre":"Licuado: Zumo de fruta, agua y azucar",
    "precio": 2000
},
{
    "tipo": "Sin alcohol",
    "nombre":"Mojito: Lima, menta y azucar",
    "precio": 4000
},
]


# -----------------------------------------------------------------------------------------------------

     #   MENU POSTRES

menus=[
{
    "tipo": "Frío",
    "nombre":"Helado",
    "precio": 3000
},
{
    "tipo": "Frío",
    "nombre":"Torta de banana split",
    "precio": 4000
},
{
    "tipo": "Frío",
    "nombre":"Torta óreo helada",
    "precio": 3500
},
{
    "tipo": "Caliente",
    "nombre":"Coulant de chocolate",
    "precio":3500
},
{
    "tipo": "Caliente",
    "nombre":"Coulant de chocolate",
    "precio":2500
},
{
    "tipo": "caliente",
    "nombre":"Pastel de manzana",
    "precio": 5500
}
]

# -------------------------------------------------------------------------------------------
               
                  # MENU COMIDAS
    
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

# --------------------------------------------------------------------------------------------

       # MENU POSTRES

menu_postre = [
{"tipo": "niño", 
 "nombre": "Brochetas de fruta", 
 "precio": 3500
 },

{"tipo": "niño",
  "nombre": "Mini hamburguesas de pollo",
  "precio": 4000
},

{"tipo": "niño", 
 "nombre": "Nuggets de pollo", 
 "precio": 3500
},

{"tipo": "niño", 
 "nombre": "Macarrones con queso", 
 "precio": 4200
},
    
{"tipo": "niño",
 "nombre": "Mini pizza",
 "precio": 3000
},

{"tipo": "adulto", 
 "nombre": "Ensalada César", 
 "precio": 4500
},
  
{"tipo": "adulto", 
 "nombre": "Sopa de cebolla francesa", 
 "precio": 4500
},

{"tipo": "adulto", 
 "nombre": "Bruschettas variadas",
 "precio": 4000
},

{"tipo": "adulto",
 "nombre": "Empanadas argentinas", 
 "precio": 3500
 },
{"tipo": "adulto", 
 "nombre": "Tabla de quesos y fiambres",
 "precio": 5500}
]

print (menu_postre)