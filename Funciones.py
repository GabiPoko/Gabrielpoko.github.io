#color1 = 'Blanco'
#color2 = 'Blanco'
#color3 = 'Negro'

#if color1 != color2 and color2 != color3 :
 #   print ('color 1 es igual a color 3')
#elif color1 != color3 and color1 != color2:
 #   print ('color2 es igual a color3')
#else:
    #print ('color1 es igual a color2')

#.---------------------------------------------------------------------------------

#num = int (input ('Ingresá un número entero: '))
#if num < 0 :
 #   print ('El número ingresado es negativo')
#elif num > 0 :
 #   print ('El número es positivo')
#else :
 #   print ('El número es 0')
    #-------------------------------------------------------------------------------

#num = int (input ('Ingresar un número entero: '))
#if num % 2 == 0 and num % 3 == 0 :
 #   print ('El número ingresado es múltiplo de 2 y 3 a la vez')
#else :
 #   print ('El número ingresado no es múltiplo de 2 y 3 a la vez')

#-------------------------------------------------------------------------------

#caracter = input('Ingresar un caracter: ')
#if caracter.isupper():
 #   print ('El caracter es una mayúscula')
#elif caracter.islower():
 #   print ('El caracter es una minúscula')
#elif caracter.isdigit ():
 #   print ('El caracter es un núemero')
#else:
 #   print ('Es un caracter especial')

#------------------------------------------------------------------------------

#numeros = [1, 2, 3, 4, 5, 6]
#for numero in numeros:
  #  print (numero)

#-------------------------------------------------------------

#texto = 'Yo volveré a las calles, se que mi barrio esprará, yo volveré a las calles, hay un lugar para estar, con vos una vez mas'
#for caracteres in texto:
  #  print (caracteres)
#-------------------------------------------------
#for i in range (6):
 #   print (i)
#-----------------------------------------------------------------
diccionario = {'a':1, 'b':2, 'c':3} #Iterar sobre claves!
#for clave in diccionario:
    #print (clave)
    #print ('---')

#----------------------------------------------

#for valores in diccionario.values(): #Iterar sobre valores
 #   print (valores)
  #  print ('---')
#----------------------------------------------------------------------------

#for clave, valor in diccionario.items(): #Para iterar clave y valor (items)
 #   print (clave, valor)

#-------------------------------------------------------------------------------

#BUCLE----> While

#contador =0

#while contador >= 5:
 #   print (contador)
  #  contador += 1
    
#----------------------------------------------------------------------------------------
# ejemplo de breack

#contador =0

#while contador <= 5:
 ##      break
   # print (contador)
    #contador += 1

    #------------------------------------------------------------------------------------

    #Ejemplo de continue

contador = 1

while contador <=5:
    if contador == 3:
       contador += 1
    continue
print(contador)
contador += 1
    