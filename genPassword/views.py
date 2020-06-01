from django.shortcuts import render

# Create your views here.
def home(request):
    rango = range(8, 51)
    return render(request, 'genPassword/home.html', {'rango':rango})

def password(request):
    if request.method == 'POST':
        passs = ""
        import string
        from random import randint, choice
        #from time import time
        letters = list(string.ascii_lowercase)
        try:
            if request.POST['Upper']:
                letters.extend(list(string.ascii_uppercase))
        except Exception as e:
            pass
        try:
            if request.POST['Digitos']:
                letters.extend(list(string.digits))
        except Exception as e:
            pass
        try:
            if request.POST['Especial']:
                letters.extend(list(string.punctuation))
        except Exception as e:
            pass
        try:
            tam =  int(request.POST['longitud'])
        except Exception as e:
            rango = range(8, 51)
            error = True
            return render(request, 'genPassword/home.html', {'rango':rango, 'error':error})

        passs = ("").join(choice(letters)for i in range(tam))
        return render(request, 'genPassword/password.html', {'pass': passs})
    else:
        rango = range(8, 51)
        return render(request, 'genPassword/home.html', {'rango':rango})

"""
def password(request):
    passs = ""
    import string
    from random import randint, choice
    from time import time
    letters = list(string.ascii_lowercase)
    if request.GET.get('Upper'):
        letters.extend(list(string.ascii_uppercase))
    if request.GET.get('Digitos'):
        letters.extend(list(string.digits))
    if request.GET.get('Especial'):
        letters.extend(list(string.punctuation))
    try:
        tam =  int(request.GET.get('longitud',12))
    except Exception as e:
        tam = 12

    passs = ("").join(choice(letters)for i in range(tam))
    return render(request, 'genPassword/password.html', {'pass': passs})
"""
