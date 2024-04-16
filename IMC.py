print('\nHola! Este programa te ayudará a conocer tu IMC (Índice de Masa Corporal)')

#Pedimos el nombre y nos aseguramos de que el usuario intrioduzca un dato, de lo contrario no podrá avanzar
#aplica lo mismo con el primer y segundo apellido
cond = False
while cond == False: 
   nombre = input('Comencemos por conocerte \n\nPor favor ingresa tu Nombre/nombres: ')
   if not nombre: 
     print(nombre)
   else: 
     cond = True
cond = False 
while cond == False:
  ap = input('Ahora tu apellido Paterno: ')
  if not ap:
    print(ap) 
  else: 
    cond = True
cond = False
while cond == False:
  am = input('Seguimos con tu apellido Materno: ')
  if not ap:
    print(ap)
  else:
    cond = True 

#Regresamos saludo al usuario mostrando en pantalla el nombre que ingresó, utilizamos la función capitaliza para
#mostrar su nombre con la primera letra en mayúscula
print('\nPara mi es un placer poder ayudarte',nombre.capitalize())
print('\nAhora tomaremos los datos relacionados con tu fisico')

#Para la toma de los siguientes datos (edad, estatura y peso) nos aseguramos de que el usuario ingrese valores
#numericos y también que estos no sean cero o menor a cero
cond = False
while cond == False:
   try:
    edad = input ('Dime por favor cuál es tu edad: ')
    edad = float (edad)  
   except ValueError:
     print('\nTu edad debe de estar escrita en números')
   else:
     edad = float(edad)
     if edad <= 0:
       print('\nNo puedes tener cero o menos años')
     if edad > 0:
      cond = True

#Se le indica al usuario cómo debe de ingresar su estatura
print('\nPara continuar es necesario conocer tu estatura \nPor favor utiliza solo números y centimetros como la unidad de medida \n\nEjemplo: Si mides 1.75m deberás teclear 175')

#De igual manera se condiciona el dato de la estatura
cond = False
while cond == False:
  try: 
    estatura = input('¿Cuánto mides?: ')
    estatura = float(estatura)
  except ValueError:
    print(estatura)
  else: 
    estatura = float(estatura)
    if estatura <= 0:
      print('Tu estatura no puede ser menor o igual a cero')
    if estatura > 0:
      cond = True

#Pedimos al usuario que ingrese su peso
print('Por último necesitaremos saber cuanto pesas')
cond = False
while cond == False:
  try:
    peso = input('\nPor favor ingresa tu peso en Kilogramos: ')
    peso = float(peso)
  except ValueError: 
    print(peso)
  else:
    peso = float (peso)
    if peso <= 0:
      print('Tu peso no puede ser menor o igual a cero')
    if peso > 0:
      cond = True

#Calculamos el IMC con los datos proporcionados por el ususario
imc = (peso/estatura**2)*10000
print('Paciente:', nombre.capitalize(), ap.capitalize(), am.capitalize(), '\nEdad:', edad, '\nEstatura:', estatura, '\nPeso:', peso,)
print('\nTu IMC es:',imc)

print('Gracias ¡Vuelve pronto!')


  
     
    


      

