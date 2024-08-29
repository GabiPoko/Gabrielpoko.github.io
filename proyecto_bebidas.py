

#Función que imprime un listado con nombre de bebida, ingrediente y precio. 



def menu_bebidas(bebidas):
    for bebida, info in bebidas.items():
        precio, ingredientes = info
        print(f'{bebida}: ${precio}')
        print(f'Ingredientes: {', '.join(ingredientes)}')
        print("-" * 30)

# # Hice un menú con bebidas alcohólicas y analcohólicas
menu_alcohol = {'Campari': [3000, ['naranja amarga, aguardiente y jarabe azucarado']], 'Martini': [2500, ['ginebra y vermú']], 'Margarita': [3000, ['tequila blanco, jugo de limón y licor de naranja']], 'Manhattan': [3500, ['Whisky con martini rojo']], 'Fernet': [2000, ['Fernet branca con gaseosa cola']]}

menu_sin_alcohol = {'Limonada':[2000, ['Limón, agua y azucar']], 'Licuado':[1500, ['Zumo de fruta y agua']], 'Mojito': [2500, ['Lima, menta y azucar']]}

menu_bebidas(menu_sin_alcohol)





