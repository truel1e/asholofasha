from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username).first()

        if user is not None and user.check_password(password):
            request.session['username'] = username
            return redirect('index')
        else:

            return render(request, 'main/login.html', {'error_message': 'Пользователь не найден.'})

    return render(request, 'main/login.html')

def myreg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'main/register.html', {'error_message': 'не надежный пароль, он должен состоять не меньше чем из 8 символов, содержать цифры, и заглавные буквы'})
    else:
        form = UserCreationForm()

    return render(request, 'main/register.html', {'form': form})

def index(request):
    dect = {
        'title': 'MeatBeat',
        'vales':['data', 'hi', 'ops']
        }
    return render(request, 'main/index.html', dect)

def about(request):
    return render(request, 'main/profil.html')

def setting(request):
    return render(request, 'main/setting.html')


