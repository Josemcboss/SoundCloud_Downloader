import os
import subprocess
import sys
from dotenv import load_dotenv

def verificar_instalacion_scdl():
    try:
        subprocess.run(['scdl', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def instalar_scdl():
    print("Instalando scdl...")
    try:
        subprocess.run(['pip', 'install', 'scdl'], check=True)
        return True
    except subprocess.CalledProcessError:
        print("Error al instalar scdl. Por favor, instálalo manualmente.")
        return False

def verificar_instalacion_ffmpeg():
    try:
        # Intentar diferentes rutas comunes de ffmpeg
        rutas_ffmpeg = [
            'ffmpeg',
            'ffmpeg.exe',
            r'C:\ffmpeg\bin\ffmpeg.exe',
            r'C:\Program Files\ffmpeg\bin\ffmpeg.exe',
            r'C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe'
        ]
        
        for ruta in rutas_ffmpeg:
            try:
                resultado = subprocess.run([ruta, '-version'], 
                                        capture_output=True, 
                                        text=True, 
                                        check=True)
                print(f"ffmpeg encontrado en: {ruta}")
                # Guardar la ruta de ffmpeg en una variable de entorno
                os.environ['PATH'] = os.path.dirname(ruta) + os.pathsep + os.environ['PATH']
                return True
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
        
        print("\nNo se pudo encontrar ffmpeg en el sistema.")
        print("Por favor, asegúrate de que ffmpeg está instalado y en el PATH del sistema.")
        print("\nPara instalar ffmpeg manualmente:")
        print("1. Windows:")
        print("   - Descarga ffmpeg desde https://ffmpeg.org/download.html")
        print("   - Extrae los archivos en C:\\ffmpeg")
        print("   - Agrega C:\\ffmpeg\\bin a las variables de entorno PATH")
        print("2. Linux: sudo apt-get install ffmpeg")
        print("3. Mac: brew install ffmpeg")
        return False
        
    except Exception as e:
        print(f"Error al verificar ffmpeg: {e}")
        return False

def instalar_ffmpeg():
    print("Intentando instalar ffmpeg...")
    try:
        if sys.platform == 'win32':
            print("Detectado sistema Windows")
            # Primero verificar si chocolatey está instalado
            try:
                subprocess.run(['choco', '-v'], capture_output=True, check=True)
                print("Instalando ffmpeg usando Chocolatey...")
                subprocess.run(['choco', 'install', 'ffmpeg', '-y'], check=True)
                # Agregar la ruta de ffmpeg al PATH
                ffmpeg_path = r'C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin'
                if os.path.exists(ffmpeg_path):
                    os.environ['PATH'] = ffmpeg_path + os.pathsep + os.environ['PATH']
            except (subprocess.CalledProcessError, FileNotFoundError):
                print("Chocolatey no está instalado. Por favor, instala ffmpeg manualmente:")
                print("1. Descarga ffmpeg desde https://ffmpeg.org/download.html")
                print("2. Extrae los archivos en C:\\ffmpeg")
                print("3. Agrega C:\\ffmpeg\\bin a las variables de entorno PATH")
                return False
        else:
            # En Linux/Mac, usamos el gestor de paquetes del sistema
            if sys.platform == 'darwin':
                print("Detectado sistema MacOS")
                subprocess.run(['brew', 'install', 'ffmpeg'], check=True)
            else:
                print("Detectado sistema Linux")
                subprocess.run(['sudo', 'apt-get', 'update'], check=True)
                subprocess.run(['sudo', 'apt-get', 'install', '-y', 'ffmpeg'], check=True)
        
        # Verificar la instalación después de intentar instalar
        if verificar_instalacion_ffmpeg():
            print("¡ffmpeg instalado correctamente!")
            return True
        else:
            print("La instalación de ffmpeg no fue exitosa.")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"Error durante la instalación de ffmpeg: {e}")
        return False
    except Exception as e:
        print(f"Error inesperado durante la instalación: {e}")
        return False

def descargar_cancion(url):
    # Intentar instalar ffmpeg si no está instalado
    if not verificar_instalacion_ffmpeg():
        print("ffmpeg no está instalado. Intentando instalar...")
        if not instalar_ffmpeg():
            print("No se pudo instalar ffmpeg. Continuando con descarga en MP3...")
            formato = '--onlymp3'
        else:
            formato = '--flac'
    else:
        formato = '--flac'
    
    try:
        # Crear directorio de descargas si no existe
        if not os.path.exists('descargas'):
            os.makedirs('descargas')
        
        # Comando para descargar la canción
        comando = [
            'scdl',
            '-l', url,
            '--path', 'descargas',
            '--name-format', '%(title)s.%(ext)s',
            formato
        ]
        
        print(f"Descargando: {url}")
        subprocess.run(comando, check=True)
        print("¡Descarga completada!")
        
    except subprocess.CalledProcessError as e:
        print(f"Error al descargar la canción: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def descargar_playlist(url):
    # Intentar instalar ffmpeg si no está instalado
    if not verificar_instalacion_ffmpeg():
        print("ffmpeg no está instalado. Intentando instalar...")
        if not instalar_ffmpeg():
            print("No se pudo instalar ffmpeg. Continuando con descarga en MP3...")
            formato = '--onlymp3'
        else:
            formato = '--flac'
    else:
        formato = '--flac'
    
    try:
        # Crear directorio de descargas si no existe
        if not os.path.exists('descargas'):
            os.makedirs('descargas')
        
        # Limpiar la URL de espacios y parámetros innecesarios
        url = url.strip()
        if '?' in url:
            url = url.split('?')[0]
        
        # Comando para descargar la playlist
        comando = [
            'scdl',
            '-l', url,
            '-p',  # Esta opción es específica para descargar playlists
            '--path', 'descargas',
            '--name-format', '%(title)s.%(ext)s',
            formato
        ]
        
        print(f"Descargando playlist: {url}")
        subprocess.run(comando, check=True)
        print("\n¡Descarga de playlist completada!")
        
    except subprocess.CalledProcessError as e:
        print(f"Error al descargar la playlist: {e}")
        print("\nSugerencias para solucionar el problema:")
        print("1. Verifica que la URL de la playlist sea correcta")
        print("2. Asegúrate de que tienes una conexión a internet estable")
        print("3. Intenta con una URL más corta (sin parámetros adicionales)")
    except Exception as e:
        print(f"Error inesperado: {e}")

def main():
    if not verificar_instalacion_scdl():
        if not instalar_scdl():
            sys.exit(1)
    
    print("=== Descargador de SoundCloud ===")
    while True:
        print("\nOpciones:")
        print("1. Descargar canción individual")
        print("2. Descargar playlist")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción (1-3): ")
        
        if opcion == "3":
            break
            
        if opcion not in ["1", "2"]:
            print("Opción no válida")
            continue
            
        url = input("\nIngresa la URL de SoundCloud: ")
        
        if 'soundcloud.com' not in url:
            print("Por favor, ingresa una URL válida de SoundCloud")
            continue
            
        if opcion == "1":
            descargar_cancion(url)
        else:
            descargar_playlist(url)

if __name__ == "__main__":
    main() 