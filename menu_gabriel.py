import tkinter as tk 

from proyecto_bebidas import *

#crear ventana
ventana = tk.Tk()
ventana.title('Comedor Grupo 2') 
ventana. geometry('500x400') 
ventana. resizable (0,0)
ventana.iconbitmap('trago.ico.ico')


#crear barra menu principal

barra_menu = tk.Menu(ventana)
ventana.config(menu= barra_menu)
menu_bebidas = tk.Menu(barra_menu)
barra_menu.add_cascade(label = 'Menu Bebidas', menu = menu_bebidas) 

#crear submenu

submenu1 = tk.Menu(menu_bebidas) 
menu_bebidas.add_cascade (label = 'Bebidas alcohólicas', menu = submenu1)
submenu1.add_cascade(label = 'Martini')
submenu1.add_separator()
submenu1.add_command(label = 'Daiquiri')
submenu1.add_separator()
submenu1.add_command(label = 'Cosmopolitan')


menu_bebidas.add_separator()

submenu2 = tk.Menu(menu_bebidas)
menu_bebidas.add_cascade (label = 'Bebidas sin alcohol', menu = submenu2)

submenu2.add_command(label = 'Licuado')
submenu2.add_separator()
submenu2.add_command(label = 'Mojito')
submenu2.add_separator()
submenu2.add_command(label = 'Limonada')


ventana.mainloop()