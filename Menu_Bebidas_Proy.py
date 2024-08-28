
#Preguntar como hacer para que la opcion del menú imprima precio e ingredientes en el mismo frame

#Ver con los chicos si agregamos boton de cerrar o volver a menu

#Ver con los chicos si agregamos alguna especie de registro de los pedidos



import tkinter as tk




class MenuBar:
    def __init__(self, ventana):
        
        self.ventana = ventana
        self.barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.barra_menu)

        self.menu_bebidas = tk.Menu(self.barra_menu)
        self.barra_menu.add_cascade(label='Menu Bebidas', menu=self.menu_bebidas)

        self.crear_submenus()

    

    def crear_submenus(self):
        self.submenu1 = tk.Menu(self.menu_bebidas)
        self.menu_bebidas.add_cascade(label='Bebidas alcohólicas', menu=self.submenu1)
        self.submenu1.add_command(label='Campari')
        self.submenu1.add_separator()
        self.submenu1.add_command(label='Daiquiri')
        self.submenu1.add_separator()
        self.submenu1.add_command(label='Cosmopolitan')

        self.menu_bebidas.add_separator()

        self.submenu2 = tk.Menu(self.menu_bebidas)
        self.menu_bebidas.add_cascade(label='Bebidas sin alcohol', menu=self.submenu2)
        self.submenu2.add_command(label='Licuado')
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