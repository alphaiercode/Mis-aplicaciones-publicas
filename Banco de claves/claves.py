import time
import random
from datetime import date
from colorama import Fore, Back
import os
import sqlite3
import getpass

class Sistema:
    os.system('mode con: cols=50 lines=30')
    print(Fore.GREEN)

    def __init__(self):
        self.dia_fecha = date.today()
        self.clave = "1"
        self.intentos = 3
        self.conexion()
        self.Login()

    def Login(self):
        print("\t\t\tFecha actual: ", self.dia_fecha, "\t")
        print("░█████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗░██████╗")
        print(" ██╔══██╗██║░░░░░██╔══██╗██║░░░██║██╔════╝██╔════╝")
        print(" ██║░░╚═╝██║░░░░░███████║╚██╗░██╔╝█████╗░░╚█████╗░")
        print(" ██║░░██╗██║░░░░░██╔══██║░╚████╔╝░██╔══╝░░░╚═══██╗")
        print(" ╚█████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██████╔╝")
        print(" ░╚════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░")

        print("\t\t\t  alphaier.code@gmail.com")
        print("\t\t\t\tVersion:0.1\t\n\n")

        print(Fore.YELLOW, "\n\t\t  ¡ATENCION! \t")
        print(Fore.YELLOW,"\t¡Lo que escriba no sera visible!\n", Fore.GREEN)
        psw = getpass.getpass("\t<Ingrese su clave para ingresar>\n\t> ")

        if psw != self.clave:
            print(Fore.RED,"\t\tClave invalida")
            time.sleep(0.5)
            os.system("cls")
            self.Login()
        else:
            self.Menu()

    def conexion(self):
        try:
            self.conexion = sqlite3.connect("datos.db")
            self.cursor = self.conexion.cursor()

            self.cursor.execute(" CREATE TABLE IF NOT EXISTS informacion (id integer PRIMARY KEY,fecha text, usuario text, clave text, sistema text); ")

        except Exception as e:
            print("Ha ocurrido un error al conectarse a la base de datos.")
            print("Desconectado sistema")
            time.sleep(1)
            exit()

    def Menu(self):
        os.system('mode con: cols=50 lines=30')
        os.system("cls")
        print("\t\t\tFecha actual: ", self.dia_fecha, "\t")
        print("░█████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗░██████╗")
        print(" ██╔══██╗██║░░░░░██╔══██╗██║░░░██║██╔════╝██╔════╝")
        print(" ██║░░╚═╝██║░░░░░███████║╚██╗░██╔╝█████╗░░╚█████╗░")
        print(" ██║░░██╗██║░░░░░██╔══██║░╚████╔╝░██╔══╝░░░╚═══██╗")
        print(" ╚█████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██████╔╝")
        print(" ░╚════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░")

        print("\t\t\t  alphaier.code@gmail.com")
        print("\t\t\t\tVersion:0.1\t\n\n")


        while True:
            try:
                print(Fore.YELLOW, "\n1. Registrar nuevo.\n\n2. Visualizar base de datos.\n\n3. Generar clave fuerte.\n\n4. Borrar todos los registros.\n\n5. Desconectar.\n\n",Fore.GREEN)
                opc = int(input(">>> "))
                if opc == 1:
                    self.Registrar()
                elif opc == 2:
                    self.visualizar_datos()
                elif opc == 3:
                    self.generar_clave()
                elif opc == 4:
                    self.borrar_todo()
                elif opc == 5:
                    print(Fore.RED, "\n\nFUERA DE LINEA", Fore.GREEN)
                    quit()
                else:
                    os.system("cls")
                    continue

            except Exception as e:
                print(e)
                print("Ha ingresado una opcion no valida.")
                time.sleep(0.3)
                os.system("cls")
                self.Menu()

    def Registrar(self):
        os.system("cls")
        print("Registrar nuevo >")
        print(Fore.YELLOW, "INGRESE 0 EN EL USUARIO PARA CANCELAR.", Fore.GREEN)

        while True:
            nom = input("\nIngrese el usuario: ")

            if nom == "0":
                self.Menu()

            if (len(nom) < 1):
                print(Fore.RED, "Debe ingresar al menos 1 caracter.", Fore.GREEN)
            else:
                break



        while True:
            clave = input("Ingrese la clave: ")
            if (len(clave) < 6):
                print(Fore.RED, "Su clave debe tener al menos 6 caracteres.", Fore.GREEN)
            else:
                break

        while True:
            sistema = input("Ingrese el origen: ")
            self.guardado_database(nom, clave, sistema)


    def guardado_database(self, nom, clave, sistema):
        self.conexion.execute("INSERT INTO informacion(fecha, usuario, clave, sistema) VALUES (?, ?, ?, ?);",(self.dia_fecha, nom, clave, sistema))

        self.conexion.commit()
        print("\nDatos registrados en la base de datos.\n")
        print(time.sleep(2))
        self.Menu()

    def visualizar_datos(self):
        os.system('mode con: cols=130 lines=30')
        os.system("cls")
        print("INFORMACION REGISTRADA>\n\n")
        lectura = self.cursor.execute("SELECT * FROM informacion")
        self.registros = 0

        for i in lectura:
            print("\tId:", i[0], "\tRegistrado: ",i[1], "\tUsuario: ", i[2], "\tClave: ", i[3], "\tOrigen: ", i[4])
            self.registros +=1

        print(Fore.YELLOW, "\n\n\tRegistros totales: ", self.registros, Fore.GREEN)

        opc = int(input("\n\n\n1. Borrar.\n2. Volver...\n\n >> "))

        if opc == 1:
            borr = input("Ingrese el ID: ")
            self.borrar_dato(borr)
        elif opc == 2:
            self.Menu()

        else:
            self.visualizar_datos()

    def borrar_dato(self, id):
        confirmacion = input("¡Esta por borrar el registro ID: "+ id + " ¿ESTA SEGURO ?[S][N]: ")
        if confirmacion == "S":
            self.cursor.execute("DELETE FROM informacion WHERE id = ?", id)
            self.conexion.commit()
            print("El registro ha sido eliminado.")

            time.sleep(0.2)
            self.visualizar_datos()
        elif confirmacion == "N":
            print("Operacion cancelada")
            self.visualizar_datos()
        else:
            self.visualizar_datos()

    def borrar_todo(self):
        confirmacion = input("¡Esta por borrar todos los registros ¿ESTA SEGURO ?[S][N]: ")
        if confirmacion == "S":
            #Borra todo.
            self.cursor.execute("DROP TABLE informacion")
            self.conexion.commit()
            print(Fore.YELLOW,"¡Se ha borrado toda la informacion!", Fore.GREEN)
            time.sleep(1)
            print(Fore.RED, "\n\t\tDESCONECTANDO")
            time.sleep(1)
            print("\tLA SESION HA FINALIZADO")
            quit()
        elif confirmacion == "N":
            self.Menu()
        else:
            borrar_dato()

    def generar_clave(self):
        os.system("cls")
        print("Generador de Claves>\n")

        letras = ("a", "b", "c", "d", "e", "f", "g", "h",
                  "i", "j", "k", "l", "m", "n", "r", "s", "t", "w", "x", "y", "z", "$", "+", "-", "%")

        dato = ""

        caracteres = str(input("¿Palabra clave?: "))

        while len(caracteres) < 2:
            print(Fore.RED, "La palabra debe tener minimo 2 caracteres.", Fore.GREEN)
            caracteres = str(input("¿Palabra clave?: "))

        while len(dato) < 15:
            letra_random = random.choice(letras)
            numero_random = random.randint(0, 10)

            dato = dato + letra_random
            dato = dato + str(numero_random)

            if len(dato) < 6:
                dato = dato + caracteres

        print(Fore.YELLOW, "\nSu nueva clave segura es:",Back.WHITE, Fore.BLACK, dato)
        print(Back.BLACK, Fore.GREEN)
        print(Fore.YELLOW, "\t\t¡ATENCION!", "\n\t¡COPIE LA CLAVE GENERADA!")
        print(Back.BLACK, Fore.GREEN)

        input("\n\nPresione una tecla para volver al menu.\n>>> ")
        self.Menu()


app = Sistema()
