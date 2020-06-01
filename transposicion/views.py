from django.shortcuts import render

import string
from random import choice

# Create your views here.
def home(request):
    rango = range(5,50)
    return render(request, 'transposicion/home.html', {'desplaza':rango})

def cifrar(mensaje, tamanio):
    tam = tamanio ** 2
    caracteres = list(string.ascii_uppercase)
    aleatorios = ("").join(choice(caracteres)for i in range( (tamanio ** 2) - len(mensaje) ))
    matriz = mensaje + aleatorios
    cifrado = ("").join(matriz[ ((i[0] * tamanio) % tam) + int(i[0] * tamanio / tam) ]for i in enumerate(matriz))
    return cifrado

def decryp(mensaje):
    tam = int( len(mensaje) ** (1/2) )
    mensaje = ("").join(mensaje[ ((i[0] * tam) % len(mensaje)) + int(i[0] * tam / len(mensaje)) ]for i in enumerate(mensaje))
    return mensaje

def transposicion(request):
    rango = range(5,50)
    if request.method == 'POST':
        error = False
        error1 =  False
        try:
            matriz =  int(request.POST['matriz'])
        except Exception as e:
            error = True
            return render(request, 'transposicion/home.html', {'desplaza':rango, 'error':error})
        try:
            mensaje = (request.POST['mensaje']).upper()
            if (len(mensaje) == 0):
                error1 = True
                return render(request, 'transposicion/home.html', {'desplaza':rango, 'error1':error1})
        except Exception as e:
            error1 = True
            return render(request, 'transposicion/home.html', {'desplaza':rango, 'error':error1})

        if (matriz ** 2 < len(mensaje)):
            error4 = True
            return render(request, 'transposicion/home.html', {'desplaza':rango, 'error4':error4})

        encrptado = cifrar(mensaje, matriz)
        return render(request, 'transposicion/transposicionEncryted.html', {'cabeza':"Tu mensaje encriptado es:", 'mensaje':encrptado})
    else:
        error3 = True
        return render(request, 'transposicion/home.html', {'desplaza':rango})

def transposicionDecryp(request):
    rango = range(5,50)
    if request.method == 'POST':
        error = False
        error1 =  False
        try:
            matriz =  int(request.POST['matriz'])
        except Exception as e:
            error = True
            return render(request, 'transposicion/transposicionDecryp.html', {'desplaza':rango, 'error':error})
        try:
            mensaje = (request.POST['mensaje']).upper()
            if (len(mensaje) == 0):
                error1 = True
                return render(request, 'transposicion/transposicionDecryp.html', {'desplaza':rango, 'error1':error1})
        except Exception as e:
            error1 = True
            return render(request, 'transposicion/transposicionDecryp.html', {'desplaza':rango, 'error':error1})

        if (len(mensaje) ** (1/2) != matriz):
            error4 = True
            return render(request, 'transposicion/transposicionDecryp.html', {'desplaza':rango, 'error4':error4})

        encrptado = decryp(mensaje)
        return render(request, 'transposicion/transposicionEncryted.html', {'cabeza':"Tu mensaje desencriptado es:", 'mensaje':encrptado})
    else:
        error3 = True
        return render(request, 'transposicion/transposicionDecryp.html', {'desplaza':rango, 'error3':error3})
