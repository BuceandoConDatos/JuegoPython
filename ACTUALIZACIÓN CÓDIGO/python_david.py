# COMENTARIOS GENERICOS CODIGO
## Todos los comentarios y texto que se especifica a lo largo del codigo esta escrito sin acentos y sin caracteres especiales con el objetivo de desarrollar buenas practicas
### Para la correcta ejecucion del codigo, descomprimir la carpeta y subir todos los archivos a una carpeta de Jupyter

# IMPORTACION DE LAS BIBLIOTECAS NECESARIAS PARA LA CORRECTA EJECUCION DEL CODIGO
# NOTA IMPORTANTE: PARA INCLUIR ELEMENTOS MUSICALES HA SIDO NECESARIO INSTALAR LA BIBLIOTECA QUE SE DETALLA, CON EL SIGUIENTE COMANDO --> !pip install pygame

# 2º NOTA IMPORTANTE: PARA UNA MEJOR EXPERIENCIA A LA HORA DE JUGAR, AMPLIAR EL CUADRO EN EL QUE SE EJECUTA.


# DEFINICION DE METODO PROPIO. SE UTILIZA PARA ENCAPSULAR LA LOGICA DEL PROYECTO Y PODER SER LLAMADO RAPIDAMENTE.

def ProyectoPython():

    # BIBLIOTECAS NECESARIAS PARA EJECUTAR PARTES DEL CODIGO (Nº ALEATORIO, OCULTACION NUMERO, GIFS, SONIDOS Y GRAFICAS)
    import random
    from getpass import getpass
    from IPython.display import display, Image, Audio
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    # Se crea un diccionario vacio para almacenar las estadisticas de jugadores
    estadisticas_jugadores = {}
    
    
    # DEFINICIÓN DE FUNCIONES
    
    # Funcion espacio a modo de organización y limpieza del código. Agrega espacios cuando se la invoca
    def espacio(n):
        print("\n" * n)
    
    # Funcion nombre para que el jugador ingrese su nombre
    def Nombre():
        nombre_valido = False
        while not nombre_valido:
            nombre_jugador = input("Hola, ¿como te llamas?: ").strip()
            if not nombre_jugador:
                print("Ese nombre parece que no vale...")
                continue
            # Se limita para que no se puedan introducir valores numericos
            if not nombre_jugador.isalpha():
                print("No se puede introducir un numero como si fuera tu nombre")
                continue
            espacio(1)
            print(f"De acuerdo!!, bienvenido {nombre_jugador}")
            if nombre_jugador not in estadisticas_jugadores:
                    estadisticas_jugadores[nombre_jugador] = {
                        'partidas_jugadas': 0,
                        'intentos_realizados': 0,
                        'partidas_ganadas': 0,
                        'partidas_perdidas': 0,
                    }
            nombre_valido = True
            return nombre_jugador
    
    
    # Funcion opciones juego ya que vamos a reutilizarla a lo largo del codigo. Muestra en pantalla las opciones del juego cada vez que se la invoca
    def OpcionesJuego():
        print("1. Partida modo solitario")
        print("2. Partida 2 Jugadores")
        print("3. Estadisticas")
        print("4. Salir")
    
    # Funcion eleccion del juego que va a querer jugar el usuario. Solo permite introducir una opcion valida y en caso de que no sea asi, se muestra un mensaje de error en pantalla
    def EleccionNumeroJuego(): 
        numero_juego_valido = False
        while not numero_juego_valido:
            try:
                NumeroJuego = int(input("¿Que modo quieres jugar?: "))
                if NumeroJuego in range(1, 5):
                    numero_juego_valido = True
                    return NumeroJuego
                else:
                    print("Esa opcion no esta entre las contempladas, introduce una opcion correcta: ")
            except ValueError: 
                print("Esa opcion no esta entre las contempladas, introduce una opcion correcta")
    
    # Funcion dificultad ya que vamos a reutilizarla a lo largo del código. Permite elegir la dificultad del juego en base al numero de intentos
    def Dificultad():
        print("1. Facil (20 intentos)")
        print("2. Medio (12 intentos)")
        print("3. Dificil (5 intentos)")
    
    # Funcion que guarda la dificultad elegida por el usuario
    def EleccionDificultadElegida():
        dificultad_valida = False
        while not dificultad_valida:
            try:
                DificultadElegida = int(input("Elige una de ellas: "))
                if DificultadElegida in range(1, 4):
                    dificultad_valida = True
                    return DificultadElegida
                else:
                    print("Esa opcion no esta contemplada, intentalo de nuevo")
            except ValueError:
                print("Esa opcion no esta entre las contempladas, introduce una opcion correcta")
    
    # Funcion que determina el numero de intentos disponibles en base a la dificultad elegida
    def Intentos(dificultad):
        if dificultad == 1:
            return 20
        if dificultad == 2:
            return 12
        if dificultad == 3:
            return 5
    
    # Funcion que ejecuta un sonido tipico ganador cuando el jugador acierta el numero
    def SonidoGanador():
        sonido = Audio('sonido_ganar.wav', autoplay=True)
        display(sonido)
    
    # Funcion que ejecuta un sonido tipico perdedor cuando el jugador no acierta el numero
    def SonidoPerder():
        sonido2 = Audio('sonido_perder.wav', autoplay=True)
        display(sonido2)
    
    # Funcion que ejecuta el juego completo
    def EjecucionJuego():
        if not estadisticas_jugadores:
            nombre_jugador = Nombre()
        else:
            nombre_jugador = list(estadisticas_jugadores.keys())[0]
        espacio(1)
        print("Estas son las opciones del juego:")
        OpcionesJuego()
        espacio(1)
        NumeroJuego = EleccionNumeroJuego()
        if NumeroJuego == 3:
            espacio(1)
            Estadisticas()
            espacio(1)
            EjecucionJuego()
        elif NumeroJuego == 4:
            espacio(1)
            Salir()
        else:
            espacio(1)
            Dificultad()
            espacio(1)
            DificultadElegida = EleccionDificultadElegida()
            espacio(1)
    
        if NumeroJuego == 1:
            intentos = Intentos(DificultadElegida)
            ModoSolitario(intentos)
        if NumeroJuego == 2:
            intentos = Intentos(DificultadElegida)
            PartidaDosJugadores(intentos)      
    
    # Primera opcion del juego
    def ModoSolitario(intentos):
        # Cada vez que el usuario juega una partida, se suma al diccionario definido previamente, al concepto "partidas jugadas"
        nombre_jugador = list(estadisticas_jugadores.keys())[0]
        estadisticas_jugadores[nombre_jugador]["partidas_jugadas"] += 1
        numero_adivinar = random.randint(1, 1000)
        
        while intentos > 0:
            try:
                numero_intento = int(input("Dime que numero crees que es el correcto: "))
                # Cada vez que el usuario consume un intento, se suma al diccionario definido previamente, al concepto "intentos realizados"
                estadisticas_jugadores[nombre_jugador]["intentos_realizados"] += 1
                # Bucle para controlar que el numero que introduce el usuario esta dentro del rango previsto
                while numero_intento not in range(1, 1001):
                    print("Ese numero no es valido, recuerda que el numero a adivinar esta entre el 1 y el 1000")
                    numero_intento = int(input("Dime que numero crees que es el correcto: "))
                # Se resta un intento del numero maximo establecido cada vez que consume una oportunidad de acertar    
                intentos -= 1
                
                if numero_adivinar == numero_intento:
                    espacio(1)
                    print(f"Enhorabuena, has acertado, efectivamente, el numero a adivinar era el {numero_adivinar}")
                    espacio(1)
                    print("GANADOR GANADOR GANADOR")
                    SonidoGanador()
                    espacio(1)
                    display(Image(filename='gif1.gif'))
                    estadisticas_jugadores[nombre_jugador]["partidas_ganadas"] += 1
                    break
                else:
                    # Mensajes para hacer mas inmersivo el juego
                    print(f"Ese no es el numero correcto. Te quedan {intentos} intentos")
                    if numero_adivinar > numero_intento:
                        print("¡¡Pista!!, el numero a adivinar es mayor que el numero que has intentado")
                    if numero_adivinar < numero_intento:
                        print("¡¡Pista!!, el numero a adivinar es menor que el numero que has intentado")
                    if numero_adivinar - 10 <= numero_intento <= numero_adivinar + 10:
                        print("¡¡Animo, estas muy cerca de acertar!!")
            except ValueError:
                print("Debes introducir un numero valido")
        else:
            espacio(1)
            print(f"Lo siento, te has quedado sin intentos y por tanto has perdido, el número a adivinar era el {numero_adivinar}")
            SonidoPerder()
            estadisticas_jugadores[nombre_jugador]["partidas_perdidas"] += 1
            espacio(1)
            display(Image(filename='gif4.gif'))
        
        espacio(1)
        print("Saliendo al menu principal... Gracias por jugar")
        espacio(1)
        print("ESPERAAAA, NO TE VAYAS, QUE PUEDES SEGUIR JUGANDO")
        display(Image(filename='gif2.gif'))
        espacio(1)
        EjecucionJuego()
    
    # Segunda opción del juego
    def PartidaDosJugadores(intentos):
        nombre_jugador = list(estadisticas_jugadores.keys())[0]
        estadisticas_jugadores[nombre_jugador]["partidas_jugadas"] += 1
        # Se definen variables de control para controlar el bucle
        numero_adivinar = None
        numero_valido = False
        
        while not numero_valido:
            try:
                numero_adivinar = int(getpass("Jugador 1, piensa un numero: "))
                if numero_adivinar in range(1, 1001):
                    numero_valido = True
                else:
                    print("Ese numero no es valido, recuerda que el numero a adivinar esta entre el 1 y el 1000")
            except ValueError:
                print("Esa opcion no es valida")
        
        while intentos > 0:
            try:
                numero_intento = int(input("Jugador 2, dime que numero crees que ha pensado el Jugador 1: "))
                estadisticas_jugadores[nombre_jugador]["intentos_realizados"] += 1
                
                while numero_intento not in range(1, 1001):
                    print("Ese numero no es valido, recuerda que el numero a adivinar esta entre el 1 y el 1000")
                    numero_intento = int(input("Dime que numero crees que es el correcto: "))
                    
                intentos -= 1
                
                if numero_adivinar == numero_intento:
                    print(f"Enhorabuena, has acertado, efectivamente, el numero a adivinar era el {numero_adivinar}")
                    espacio(1)
                    print("GANADOR GANADOR GANADOR")
                    SonidoGanador()
                    espacio(1)
                    display(Image(filename='gif3.gif'))
                    estadisticas_jugadores[nombre_jugador]["partidas_ganadas"] += 1
                    break
                else:
                    print(f"Ese no es el numero correcto. Te quedan {intentos} intentos")
                    if numero_adivinar > numero_intento:
                        print("¡¡Pista!!, el numero a adivinar es mayor que el numero que has intentado")
                    if numero_adivinar < numero_intento:
                        print("¡¡Pista!!, el numero a adivinar es menor que el numero que has intentado")
                    if numero_adivinar - 10 <= numero_intento <= numero_adivinar + 10:
                        print("¡¡Animo, estas muy cerca de acertar!!")
            except ValueError:
                print("Debes introducir un numero valido")
        else:
            espacio(1)
            print(f"Lo siento, te has quedado sin intentos y por tanto has perdido, el numero a adivinar era el {numero_adivinar}")
            SonidoPerder()
            estadisticas_jugadores[nombre_jugador]["partidas_perdidas"] += 1
            espacio(1)
            display(Image(filename='gif4.gif'))
        
        print("Saliendo al menu principal... Gracias por jugar")
        espacio(1)
        print("ESPERA, NO TE VAYAS, QUE PUEDES SEGUIR JUGANDO")
        espacio(1)
        display(Image(filename='gif2.gif'))
        espacio(1)
        EjecucionJuego()
    
    # Tercera opción del juego
    def Estadisticas():
        # Para incluir las estadisticas del jugador
        if estadisticas_jugadores[list(estadisticas_jugadores.keys())[0]]["partidas_jugadas"] == 0:
            # Condicion para evitar mostrar estadisticas en caso de que no se haya jugado ninguna partida
            print("Por el momento no se muestran estadisticas porque no se ha jugado, tienes que jugar al menos una vez para que se generen.")
        else:
            nombre_jugador = list(estadisticas_jugadores.keys())[0]
            print("ESTADISTICAS JUEGO")
            espacio(1)
            print(f"Estadísticas de {nombre_jugador}")
            print(f"Partidas jugadas: Has jugado un total de {estadisticas_jugadores[nombre_jugador]['partidas_jugadas']} partida/s")
            print(f"Partidas ganadas: Has ganado un total de {estadisticas_jugadores[nombre_jugador]['partidas_ganadas']} partida/s")
            print(f"Intentos utilizados: Has realizado un total de {estadisticas_jugadores[nombre_jugador]['intentos_realizados']} intento/s")
            print(f"Partidas perdidas: Has perdido un total de {estadisticas_jugadores[nombre_jugador]['partidas_perdidas']} partida/s")
    
            # Se muestra un pequeño grafico muy visual de las partidas que se han jugado y los intentos que se han necesitado para acertar
            print("Te detallo una pequeña grafica de las partidas y los intentos utilizados")
            intentos = estadisticas_jugadores[nombre_jugador]['intentos_realizados']
            partidas_jugadas = estadisticas_jugadores[nombre_jugador]['partidas_jugadas']
            partidas_ganadas = estadisticas_jugadores[nombre_jugador]['partidas_ganadas']
            partidas_perdidas = estadisticas_jugadores[nombre_jugador]['partidas_perdidas']
    
            categorias = ['Intentos', 'Partidas Jugadas', 'Partidas Ganadas', 'Partidas Perdidas']
            valores = [intentos, partidas_jugadas, partidas_ganadas, partidas_perdidas]

            # Paleta de colores obtenida de internet, para no importar la libreria seaborn
            colores = ['#FFB3BA', '#FFDFBA', '#B2BB', '#BAFFC9']
            
            plt.figure(figsize=(10, 6))
            plt.bar(categorias, valores, color=colores)
            
            plt.title("Grafico de Estadisticas del Juego", fontsize=16)
            plt.xlabel("Categorías", fontsize=14)
            plt.ylabel("Cantidad", fontsize=14)
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
            # Para que los nombres no se solapen
            plt.tight_layout()
            plt.show()
    
            # Creacion de un df para posteriormente exportar los datos a un archivo xlsx
            datos_excel = {
                'Conceptos': [
                    'Nombre Jugador',
                    'Partidas jugadas',
                    'Partidas ganadas',
                    'Intentos utilizados',
                    'Partidas perdidas'
                ],
                'Valor': [
                    nombre_jugador,
                    estadisticas_jugadores[nombre_jugador]['partidas_jugadas'],
                    estadisticas_jugadores[nombre_jugador]['partidas_ganadas'],
                    estadisticas_jugadores[nombre_jugador]['intentos_realizados'],
                    estadisticas_jugadores[nombre_jugador]['partidas_perdidas']
                ]
            }
    
            confirmacion_estadistica = input("¿Quieres exportar todas las estadisticas a un excel? (SI/NO)\n")
            espacio(1)
            # Se define este bucle para evitar que el usuario introduzca una respuesta que no se ha contemplado
            while confirmacion_estadistica not in ('SI', 'NO'):
                print("Esa opcion no es valida, por favor, especifica si deseas salir del juego o no")
                confirmacion_estadistica = input("¿Quieres ver todas las estadisticas? (SI/NO)\n")
    
            # Se establece ruta generica de descarga, independiente del usuario que ejecute el codigo
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            if not os.path.exists(desktop):
                desktop = os.path.expanduser("~")
                print(f"No se encontró la carpeta Desktop. Se usará la carpeta de usuario: {desktop}")
            ruta_archivo = os.path.join(desktop, "estadisticas_juego.xlsx")
            ruta_archivo_filtrado1 = os.path.join(desktop, "partidas_jugadas_filtro.xlsx")
            ruta_archivo_filtrado2 = os.path.join(desktop, "partidas_ganadas_filtro.xlsx")
            ruta_archivo_filtrado3 = os.path.join(desktop, "intentos_utilizados_filtro.xlsx")
            ruta_archivo_filtrado4 = os.path.join(desktop, "partidas_perdidas_filtro.xlsx")
            # Opcion para exportar todas las estadisticas
            if confirmacion_estadistica == 'SI':
                              
                df = pd.DataFrame(datos_excel)
                df.to_excel(ruta_archivo, index=False)
                espacio(1)
                # Mensajes de ayuda al usuario para que sepa ciertamente donde se encuentra el archivo
                print("Se esta generando un archivo en formato 'xlsx' para que puedas ver todas las estadisticas...")
                print(f"El archivo se ha guardado en la siguiente ruta: {ruta_archivo}")
                espacio(1)
            else:
                # Posibilidad de filtrar en base a ciertos campos
                confirmacion_estadistica = 'NO'
                opcion_filtro = input("De acuerdo, ¿que campo quieres filtrar? (Partidas Jugadas/ Partidas Ganadas/ Intentos Utilizados/ Partidas Perdidas")
                espacio(1)
    
                # Se define este bucle para evitar que el usuario introduzca una respuesta que no se ha contemplado
                while opcion_filtro not in ('Partidas Jugadas', 'Partidas Ganadas', 'Intentos Utilizados', 'Partidas Perdidas'):
                    print("Esa opcion no es valida, por favor, especifica un filtro correcto")
                    opcion_filtro = input("De acuerdo, ¿que campo quieres filtrar? (Partidas Jugadas/ Partidas Ganadas/ Intentos Utilizados/ Partidas Perdidas")
                
                df = pd.DataFrame(datos_excel)
                
                if opcion_filtro == 'Partidas Jugadas':
                    filtro = df[df['Conceptos'] == 'Partidas jugadas']
                    filtro.to_excel(ruta_archivo_filtrado1, index=False)
                    print("Se esta generando un archivo en formato 'xlsx' unicamente con las partidas jugadas")
                    espacio(1)
                    print("Se esta generando un archivo en formato 'xlsx' para que puedas ver todas las estadisticas de partidas jugadas...")
                    print(f"El archivo se ha guardado en la siguiente ruta: {ruta_archivo_filtrado1}")
                elif opcion_filtro == 'Partidas Ganadas':
                    filtro = df[df['Conceptos'] == 'Partidas ganadas']
                    filtro.to_excel(ruta_archivo_filtrado2, index=False)
                    print("Se esta generando un archivo en formato 'xlsx' unicamente con las partidas ganadas")
                    print(f"El archivo se ha guardado en la siguiente ruta: {ruta_archivo_filtrado2}")
                    espacio(1)
                elif opcion_filtro == 'Intentos Utilizados':
                    filtro = df[df['Conceptos'] == 'Intentos utilizados']
                    filtro.to_excel(ruta_archivo_filtrado3, index=False)
                    print("Se esta generando un archivo en formato 'xlsx' unicamente con los intentos realizados")
                    print(f"El archivo se ha guardado en la siguiente ruta: {ruta_archivo_filtrado3}")
                    espacio(1)
                elif opcion_filtro == 'Partidas Perdidas':
                    filtro = df[df['Conceptos'] == 'Partidas perdidas']
                    filtro.to_excel(ruta_archivo_filtrado4, index=False)
                    print("Se esta generando un archivo en formato 'xlsx' unicamente con las partidas perdidas")
                    print(f"El archivo se ha guardado en la siguiente ruta: {ruta_archivo_filtrado4}")
                    espacio(1)
                    
                    print(f"El archivo con las estadísticas filtradas por {opcion_filtro} se ha guardado con éxito.")
                    espacio(1)
        
    # Cuarta opción del juego
    def Salir():
        pregunta_confirmacion = input("¿Estas seguro que quieres salir del juego? (SI/NO)\n")
        espacio(1)
        # Se define este bucle para evitar que el usuario introduzca una respuesta que no se ha contemplado
        while pregunta_confirmacion not in ('SI', 'NO'):
            print("Esa opcion no es valida, por favor, especifica si deseas salir del juego o no")
            pregunta_confirmacion = input("¿Estas seguro que quieres salir del juego? (SI/NO)\n")
        if pregunta_confirmacion == 'SI':
            espacio(1)
            print("Saliendo del juego... Muchas gracias por jugar")
            espacio(1)
            display(Image(filename='gif5.gif'))
        else:
            print("Volviendo al menu principal")
            espacio(1)
            EjecucionJuego()
    
    print("Practica del modulo: PROGRAMACION PYTHON\n\nADIVINA EL JUEGO")
    print("El juego consiste en adivinar un numero del 1 al 1000. Ten paciencia y se estrategico. Mucha suerte")
    
    
    espacio(1)
    
    EjecucionJuego()
