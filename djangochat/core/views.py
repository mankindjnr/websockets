from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm

# Create your views here.
def index(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')


            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                print("Logged in")
                return redirect('index')
        else:
            print(form.errors)

    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print("Logged in")
            return redirect('index')
        else:
            print("Wrong credentials")

    return render(request, 'core/signin.html')

def logout_view(request):
    logout(request)
    return redirect('index')