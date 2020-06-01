from django.shortcuts import render
import string
# Create your views here.
def home(request):
    rango = range(0,27)
    return render(request, 'cesar/cesar.html', {'desplaza':rango})

def cesarEncrypted(request):
    if request.method == 'POST':
        upper = list(string.ascii_uppercase)
        error = False
        error1 =  False
        rango = range(0,27)
        #upper.insert(upper.index('N')+1, 'Ñ')
        try:
            recorrido =  int(request.POST['desplazamiento'])
        except Exception as e:
            error = True
            return render(request, 'cesar/cesar.html', {'desplaza':rango, 'error':error})

        try:
            mensaje = (request.POST['mensaje']).upper()
            if (len(mensaje) == 0):
                error1 = True
                return render(request, 'cesar/cesar.html', {'desplaza':rango, 'error1':error1})

        except Exception as e:
            error1 = True
            return render(request, 'cesar/cesar.html', {'desplaza':rango, 'error':error1})

        encrptado = ""
        for x in mensaje:
            encrptado += " " if (x == " ") else upper[ (upper.index(x) + recorrido) % len(upper) ]
        return render(request, 'cesar/cesarEncryted.html', {'mensaje':encrptado})
    else:
        error3 = True
        return render(request, 'cesar/cesar.html', {'desplaza':rango, 'error':error})

def cesarDecrypted(request):
    rango = range(0,27)
    if request.method == 'POST':
        upper = list(string.ascii_uppercase)
        try:
            recorrido =  int(request.POST['desplazamiento'])
        except Exception as e:
            error = True
            return render(request, 'cesar/cesarDecrypted.html', {'desplaza':rango, 'error':error})
        try:
            encryp = (request.POST['mensaje']).upper()
        except Exception as e:
            error1 = True
            return render(request, 'cesar/cesarDecrypted.html', {'desplaza':rango, 'error1':error1})
        if (len(encryp) == 0):
            return render(request, 'cesar/cesarDecrypted.html', {'desplaza':rango, 'error1':True})
        mensajes = []
        if (recorrido == 27):
            for i in range(0,26):
                decryp = ""
                for x in encryp:
                    decryp += " " if (x == " ") else upper[ (upper.index(x) - i) % len(upper) ]
                mensajes.append([decryp, i])
        else:
            decryp = ""
            for x in encryp:
                decryp += " " if (x == " ") else upper[ (upper.index(x) - recorrido) % len(upper) ]
            mensajes.append([decryp, recorrido])
        return render(request, 'cesar/cesarDecryptedAll.html', {'mensajes':mensajes})
    else:
        return render(request, 'cesar/cesarDecrypted.html', {'desplaza': rango})
