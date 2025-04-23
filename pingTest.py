import subprocess
import platform

def test(direccion_ip):

    comando = ['ping']

    # Añadimos la opción para limitar el número de pings según el sistema operativo
    sistema = platform.system().lower()
    if sistema == 'windows':
        comando.extend(['-n', '4'])  # Envía 4 pings en Windows
    elif sistema == 'linux' or sistema == 'darwin':  # macOS también es Darwin
        comando.extend(['-c', '4'])  # Envía 4 pings en Linux/macOS
    else:
        print(f"Sistema operativo no reconocido: {sistema}. Intentando sin límite de pings.")

    comando.append(direccion_ip)

    # Ejecutamos el comando con un tiempo de espera
    try:
        proceso = subprocess.run(comando, capture_output=True, text=True, check=True, timeout=10) # Añadimos un tiempo máximo de 10 segundos
        print(f"Resultado del ping a {direccion_ip}:")
        print(proceso.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al hacer ping a {direccion_ip}:")
        print(e.stderr)
    except subprocess.TimeoutExpired:
        print(f"El ping a {direccion_ip} tardó demasiado en responder.")

test("8.8.8.8")