from django.shortcuts import render
from .utils import get_posts
import json
import sys
import requests
import string
# Create your views here.


def post_list(request):
    # Llamamos a la funcion get_post()
    listaDeGastos = get_posts()
    """
    La función json.dumps() convierte un objeto Python en una cadena de texto en formato JSON.
      En este caso, está convirtiendo la lista listaDeGastos en una cadena de texto en formato JSON.
    """
    postsListo = json.dumps(
        listaDeGastos)  # convertioms el objeto json en texto
    posts = postsListo.replace('\\', '')  # reemplazamos el caracter \ por ''

    # recuperamos el valor de la propiedad MSGDES del objeto JSON listaDeGastos y lo imprimimos por consola
    print("MSGDES: ", listaDeGastos["MSGDES"])

    msgdes = json.dumps(listaDeGastos["MSGDES"])

    if msgdes == 'Transacción Exitosa':
        print(msgdes)
    else:
        print('Transacción Fallida')

        # Analizamos el string JSON dentro de la propiedad "JSONRESP" del objeto JSON
        objeto = json.loads(listaDeGastos['JSONRESP'])
        # Accedemos a la propiedad "Array" del objeto JSON resultante
        array = objeto['Array']
        # Mostramos el array por consola
        print('Arreglo', array)
        # Accedemos al primer elemento del array y a su propiedad "DESG1"
        desg1 = objeto['Array'][0]['DESG1']
        # Mostramos la propiedad "DESG1" por consola
        print("Propiedad desg1:", desg1)

    return render(request, 'post_list.html', {'posts': posts, 'msgdes': msgdes})


# request es el objeto HTTP request que se ha recibido de hacer la solicitud http
# post_list.html es el nombre de la plantilla HTML que se desea renderizar
# {'posts': posts} es un diccionario que contiene los datos que se utilizarán para renderizar la plantilla


def consultar(request):
    if request.method == 'POST':
        # Recibimos los datos enviados por el usuario desde el formulario
        fecha = request.POST.get('fecha')
        numcre = request.POST.get('numcre')
        conse = request.POST.get('conse')
        f = type(fecha).__name__  # sabemos el tipo
        f1 = sys.getsizeof(f)  # sabemos el tamaño
        c = type(conse).__name__
       
        fecha = fecha.replace(" ", "")
        numcre = numcre.replace(" ", "")
        conse = conse.replace(" ", "")
        conse = conse.strip()
        numcre = " ".join(["", numcre])
        print("El texto FECHA tiene", len(fecha), "caracteres")
        print("El texto NUMCRE tiene", len(numcre), "caracteres")
        print("El texto CONSE tiene", len(conse), "caracteres")
        
        print("fecha tipo", f)
        print("El tipo conse es", c)
        print("fecha tamaño original", f1)
        print("fecha tamaño sin espacios", fecha)
       

        # Construimos la consulta a la API utilizando los datos recibidos
        # consulta = f'https://api-ejemplo.com/usuarios?nombre={nombre}&apellido={apellido}'
        url = 'http://192.168.0.3:7303/web/services/CONS_Credito/CONS_Credito'

        payload = json.dumps({
            "FECHAE": fecha,
            "NUMCREE": numcre,
            "CONSECE": conse
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        # Enviamos la consulta a la API utilizando la librería "requests"
        respuesta = requests.post(url=url, headers=headers, data=payload)
        print("respuesta", respuesta)

        response = requests.request("POST", url, headers=headers, data=payload)
        print('response de texto', response.text)

        payload1 = dict(FECHAE="23112022", NUMCREE="72207013")
        r = requests.post(url, data=payload1)
        print("payload1", r.text)
        
        # Mostramos los datos devueltos por la API en una plantilla de Django
        return render(request, 'resultado.html', {'datos': response})

    # Si el método HTTP no es POST, mostramos el formulario vacío
    return render(request, 'formulario.html')
