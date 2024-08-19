
# Intendando crear un menú con una clase Menu_bebida

class MenuAlcohol:
    def __init__(self):
        self.menu = {'Campari': [3000, ['naranja amarga, aguardiente y jarabe azucarado']],
                    'Martini': [2500, ['ginebra y vermú']], 'Margarita': [3000, ['tequila blanco, jugo de limón y licor de naranja']], 
                    'Manhattan': [3500, ['Whisky con martini rojo']], 'Fernet': [2000, ['Fernet branca con gaseosa cola']]}
 
    def menu_mostrar (self):
        print ('MENU BEBIDAS')
        for bebida, info in self.menu.items():
           precio, ingredientes = info
           print(f'{bebida}: ${precio}')
           print(f'Ingredientes: {', '.join(ingredientes)}')
           print("-" * 30)

menu = MenuAlcohol()
menu.menu_mostrar ()