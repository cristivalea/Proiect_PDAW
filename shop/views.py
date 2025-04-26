from django.shortcuts import render, get_object_or_404
from .models import Laptop
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User


# def index(request):
#     laptops = Laptop.objects.all()
#     context = {
#         'laptops': laptops
#     }
#     return render(request, 'shop/index.html', context)

def index(request):
    return render(request, 'shop/index.html')
def product_detail(request, serielaptop):
    laptop = get_object_or_404(Laptop, serielaptop=serielaptop)
    context = {
        'laptop': laptop
    }
    return render(request, 'shop/product_detail.html', context)

def cart(request):
    # Pentru început, o pagină simplă, se poate extinde ca funcționalitate de coș.
    return render(request, 'shop/cart.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Nu salvăm încă în DB
            # Adăugăm câmpurile suplimentare
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            if form.cleaned_data.get('is_admin'):
                user.is_staff = True
            user.is_active = True  # În caz că vrei să gestionezi activarea manual
            user.save()

            messages.success(request, 'Contul a fost creat cu succes! Te poți loga acum.')
            return redirect('login')
        else:
            print("Erori formular:", form.errors)
            messages.error(request, 'Ceva nu a mers bine. Te rugăm să încerci din nou.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'shop/register.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser or user.is_staff:
                # Dacă este admin sau staff, redirecționează către pagina de admin
                return redirect('admin_dashboard')  # O pagină specială pentru admini
            else:
                # Dacă e utilizator normal
                return redirect('/')
        else:
            # Dacă username sau parola sunt greșite
            return render(request, 'shop/login.html', {'error': 'Utilizator sau parolă greșită'})

    return render(request, 'shop/login.html')

from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def admin_dashboard(request):
    return render(request, 'shop/admin_dashboard.html')

from django.shortcuts import render, redirect
from .forms import LaptopForm



def adaugare_laptop(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()  # Salvează laptopul în tabela laptopuri
            return redirect('admin-dashboard')  # După ce salvezi, redirecționează spre dashboard
    else:
        form = LaptopForm()

    return render(request, 'shop/adaugare_laptop.html', {'form': form})

