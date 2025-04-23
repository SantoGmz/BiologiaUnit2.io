# **************************************************************************************
# **************************************************************************************
#
#                        * * * S A N T O S   -   S O T N A S   * * *
#
# **************************************************************************************
# **************************************************************************************
# 
#aprender smtp, usar timer, usar api de microtik, convinar con jango, usar os, usar cmd para linux y windows







# --- Sección principal de las importaciones de los modulos necesarios

import tkinter as tk
import re #esta es para buscar expresiones regulares, buscar cosas simbolso especificos
import subprocess



# **************************************************************************************
# **************************************************************************************
#
#                        * * * S A N T O S   -   S O T N A S   * * *
#
# **************************************************************************************
# **************************************************************************************
#
# --- Sección principal de las funciones 

#para saber si son ip
def verificarIP(texto):
    #Estoy usando la libreria re, estoy indicando que es de 3 en 3 separado por puntos
    patron = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    return bool(re.match(patron, texto))



# Botón para obtener el texto de los campos 
def obtener_texto():
    datos = campo_ip.get()
    

    if verificarIP == True:
        print(f"La IP {verificarIP(datos)} es válida.")

    else:
        print(f"La IP {verificarIP(datos)} no es válida.")


def hacer_ping(direccion_ip):
    comando = ['ping', direccion_ip]

    # Ejecutamos el comando
    proceso = subprocess.run(comando, capture_output=True, text=True, check=True)

    print(f"Resultado del ping a {direccion_ip}:")
    print(proceso.stdout)


''' Tengo que hacer funciones para

-hacer los pings a routers
-averiguar como hago para hacer un alert commo en javascript
-tiene que haber una forma para que cuando no reciba internet guarde el tiempo que hay por caida
-



'''

# **************************************************************************************
# **************************************************************************************
#
#                        * * * S A N T O S   -   S O T N A S   * * *
#
# **************************************************************************************
# **************************************************************************************
#
# --- Sección principal de TKinter y sus disenos

ventana = tk.Tk()
ventana.title("verificador de averias")
ventana.geometry("300x100")

# Crear etiquetas para los campos de texto
etiqueta_Dir_IP = tk.Label(ventana, text="Direccion IP:")


# Crear los campos de texto (Entry widgets)
campo_ip = tk.Entry(ventana)


# Colocar los widgets en la ventana usando el administrador de diseño 'grid'
etiqueta_Dir_IP.grid(row=0, column=0, padx=5, pady=5, sticky="w")
campo_ip.grid(row=0, column=1, padx=5, pady=5, sticky="w")







    
    
    
    



boton_obtener = tk.Button(ventana, text="Obtener Datos", command=obtener_texto)
boton_obtener.grid(row=1, column=0, columnspan=2, pady=10)

ventana.mainloop()