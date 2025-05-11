# SoundCloud Downloader

Un script en Python para descargar canciones y playlists de SoundCloud de manera sencilla.

## Características

- Descarga canciones individuales y playlists completas
- Soporte para formato FLAC (alta calidad) y MP3
- Instalación automática de dependencias (ffmpeg)
- Interfaz de línea de comandos fácil de usar
- Manejo automático de errores y reintentos

## Requisitos

- Python 3.6 o superior
- scdl (se instala automáticamente)
- ffmpeg (opcional, se instala automáticamente para formato FLAC)

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/soundcloud-downloader.git
cd soundcloud-downloader
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecuta el script:
```bash
python soundcloud_downloader.py
```

2. Selecciona una opción:
   - 1: Descargar canción individual
   - 2: Descargar playlist
   - 3: Salir

3. Ingresa la URL de SoundCloud cuando se te solicite.

Las canciones se descargarán en la carpeta `descargas` con el siguiente formato:
- Nombre del archivo: `título_de_la_canción.extensión`
- Formato: FLAC (si ffmpeg está disponible) o MP3

## Características Técnicas

- Detección automática de ffmpeg
- Instalación automática de dependencias
- Manejo de errores robusto
- Soporte para diferentes sistemas operativos
- Limpieza automática de URLs

## Solución de Problemas

### Error: "ffmpeg no está instalado"
El programa intentará instalar ffmpeg automáticamente. Si falla, puedes instalarlo manualmente:

- Windows:
  1. Descarga ffmpeg desde https://ffmpeg.org/download.html
  2. Extrae los archivos en C:\ffmpeg
  3. Agrega C:\ffmpeg\bin a las variables de entorno PATH

- Linux:
```bash
sudo apt-get install ffmpeg
```

- Mac:
```bash
brew install ffmpeg
```

### Error: "No se puede descargar la playlist"
- Verifica que la URL sea correcta
- Asegúrate de tener una conexión a internet estable
- Intenta con una URL más corta (sin parámetros adicionales)

## Contribuir

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz un Fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Tu Nombre - [@tutwitter](https://twitter.com/tutwitter) - email@ejemplo.com

Link del Proyecto: [https://github.com/tu-usuario/soundcloud-downloader](https://github.com/tu-usuario/soundcloud-downloader) 