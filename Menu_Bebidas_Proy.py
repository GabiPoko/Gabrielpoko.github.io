import tkinter as tk

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
Licuado = BebidasMenu('Licuado', 3000, 'Zumo de Fruta y agua')
Mojito = BebidasMenu ('Mojito', 2000, 'Lima, menta y azucar')


class MenuBar (BebidasMenu):
    def __init__(self, ventana):
        self.ventana = ventana
        self.barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.barra_menu)

        self.menu_bebidas = tk.Menu(self.barra_menu)
        self.barra_menu.add_cascade(label='Menu Bebidas', menu=self.menu_bebidas)

        self.create_submenus()

    def create_submenus(self):
        self.submenu1 = tk.Menu(self.menu_bebidas)
        self.menu_bebidas.add_cascade(label='Bebidas alcohólicas', menu=self.submenu1)
        self.submenu1.add_cascade(label='Martini')
        self.submenu1.add_separator()
        self.submenu1.add_command(label='Daiquiri')
        self.submenu1.add_separator()
        self.submenu1.add_command(label='Cosmopolitan')

        self.menu_bebidas.add_separator()

        self.submenu2 = tk.Menu(self.menu_bebidas)
        self.menu_bebidas.add_cascade(label='Bebidas sin alcohol', menu=self.submenu2)
        self.submenu2.add_command(label='Licuado', command= Licuado.mostrar_bebida())
        self.submenu2.add_separator()
        self.submenu2.add_command(label='Mojito')
        self.submenu2.add_separator()
        self.submenu2.add_command(label='Limonada')


class BebidasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Comedor Grupo 2')
        self.ventana.geometry('500x400')
        self.ventana.resizable(0, 0)
        self.ventana.iconbitmap('trago.ico.ico')

        self.menu_bar = MenuBar(self.ventana)

        
        self.ventana.mainloop()

app = BebidasApp()