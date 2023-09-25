import argparse
import requests
from tqdm import tqdm


parser=argparse.ArgumentParser(description="Script de fuzzing de directorios web")
parser.add_argument("url", help="URL base para el fuzzing")
parser.add_argument("diccionario", help="Archivo de diccionario")
args=parser.parse_args()

with open(argparse.diccionario) as file:
    wordlist = file.read().splitlines()

try:
    barra = tqdm(total=len(wordlist), desc="Progreso", unit="urls", dynamic_ncols=True)
    for linea in wordlist:
        url_completa = args.url + linea
        response =requests.get(url_completa)
        if response.status_code ==200:
            tqdm.write(f"Directorio encontrado: {url_completa}")
        barra.update(1)    
except KeyboardInterrupt:
    print("\n Script Interrumpido al pulsar control C")
finally:
    barra.close()