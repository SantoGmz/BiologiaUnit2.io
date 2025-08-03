#este script es para eliminar publicaciones de facebook
import pyautogui 
import time

time.sleep(0)

'''
try:
    busco = pyautogui.locateOnScreen('fb-btn-option.png')
    if busco is not None:
        print("Se encontro en: ", busco)
    else:
        print("No se encontro")    
except  Exception as e:
    print(f"Error: {e}")
    
'''
    
    
try:
    verificarBtnOpciones = pyautogui.locateOnScreen('fb-btn-option.png')    
except Exception as e:
    print(f"No se encontro el boton de opciones.")
    





def borrardor():
    
    
    pyautogui.click('fb-btn-option.png')
    
    verificarBtnTransh = pyautogui.locateOnScreen('fb-btn-trash.png')    

        
        #click al btn de basura\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    if verificarBtnTransh is not None:
        pyautogui.click('fb-btn-trash.png')
        print("Encontro el safacon")
    else:
        print("No Encontro el safacon")
        time.sleep(2)

        #############################Confirmar borrado

        #click en el btn confirmar
    pyautogui.waitFor("fb-btn-move.png", timeout=10)
    verificarBtnMove = pyautogui.locateOnScreen('fb-btn-move.png')   
    if verificarBtnMove is not None:
        pyautogui.click('fb-btn-move.png')
    else:
        time.sleep(2)
        pyautogui.click('fb-btn-move.png')
#############################Confirmar borrado
        
        
        


if verificarBtnOpciones is not None:

    borrardor()
else:
    print("No se encontro el boton opciones.")
    time.sleep(2)
    borrardor()
    






pyautogui.waitFor()