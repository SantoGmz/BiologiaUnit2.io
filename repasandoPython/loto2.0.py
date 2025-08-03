import requests
from bs4 import BeautifulSoup

def obtener_numeros_loto_mas():
    """
    Extrae los números ganadores del Loto Más de la página de Conectate.com.do.
    """
    url = "https://www.conectate.com.do/loterias/leidsa/loto-mas"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        scores_div = soup.find('div', class_='game-scores ball-mode')
        
        if scores_div:
            numeros_span = scores_div.find_all('span', class_='score')
            # Extraemos los primeros 6 números, que son los de la Loto
            numeros_loto = {int(n.text.strip()) for n in numeros_span[:6]}
            return numeros_loto
        else:
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la página: {e}")
        return None

# --- Revisa tus boletos ---
def revisar_boletos():
    """
    Combina la extracción de números ganadores con la verificación de boletos.
    """
    # Obtenemos los números ganadores
    numeros_ganadores = obtener_numeros_loto_mas()

    if not numeros_ganadores:
        print("No se pudo obtener los números ganadores de la página web. No se puede continuar la verificación.")
        return

    # Tus boletos (puedes editar esta lista con tus jugadas)
    boletos = [
        [7, 20, 26, 27, 28, 34],
        [2, 7, 15, 17, 24, 29],
        [11, 12, 13, 16, 21, 32],
        [15, 17, 28, 30, 36, 37],
        [19, 12, 20, 23, 24, 30],
        [7, 13, 15, 17, 25, 27],
        [9, 17, 31, 34, 35, 37],
        [5, 16, 27, 30, 34, 39],
        [4, 10, 16, 19, 20, 38],
        [3, 11, 12, 16, 19, 38],
    ]

    print("¡Vamos a ver cómo te fue con esos números!")
    print(f"Los números que salieron son: {' '.join(map(str, sorted(list(numeros_ganadores))))}")
    print("Aquí están tus jugadas y los aciertos en cada una:")
    print("-" * 30)

    # Itera sobre cada boleto y revisa los aciertos
    for boleto in boletos:
        boleto_set = set(boleto)
        aciertos = boleto_set.intersection(numeros_ganadores)
        
        linea_boleto = " ".join([str(num) for num in boleto])
        aciertos_str = ', '.join(map(str, sorted(list(aciertos))))
        
        if len(aciertos) == 1:
            print(f"{linea_boleto} ({len(aciertos)} acierto: {aciertos_str})")
        elif len(aciertos) > 1:
            print(f"{linea_boleto} ({len(aciertos)} aciertos: {aciertos_str})")
        else:
            print(f"{linea_boleto} (0 aciertos)")

# Llama a la función principal para ejecutar el script
revisar_boletos()