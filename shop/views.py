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
            laptop = form.save(commit=False)  # nu salva încă
            laptop.nota_produs = 0  # Default - de exemplu 0
            laptop.save()  # acum salvează
            return redirect('admin_dashboard')
    else:
        form = LaptopForm()

    return render(request, 'shop/adaugare_laptop.html', {'form': form})


from django.shortcuts import render
from .models import Laptop  # Numele modelului trebuie să corespundă cu cel din models.py


def cautare_laptop(request):
    laptopuri = None
    marca = None

    if request.method == 'POST':
        marca = request.POST.get('marca', '').strip()
        if marca:
            # Căutăm atât în Brand cât și în Model
            laptopuri = Laptop.objects.filter(brand__icontains=marca) | Laptop.objects.filter(
                model__icontains=marca)

    return render(request, 'shop/cautare_laptop.html', {
        'laptopuri': laptopuri,
        'marca': marca
    })

from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Laptop

@csrf_exempt  # doar temporar, dacă nu funcționează cu tokenul CSRF, dar e mai bine să-l păstrezi în formular!
def delete_laptop(request):
    if request.method == "POST":
        serial = request.POST.get("serielaptop")
        laptop = get_object_or_404(Laptop, serielaptop=serial)
        laptop.delete()
        return redirect('/admin-dashboard/cautare_laptop/')
    else:
        return redirect('/admin-dashboard/cautare_laptop/')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop

def edit_laptop(request, serielaptop):
    laptop = get_object_or_404(Laptop, serielaptop=serielaptop)

    if request.method == 'POST':
        laptop.nume = request.POST.get('nume')
        laptop.pret = request.POST.get('pret')
        laptop.memorie_ram = request.POST.get('memorie_ram')
        laptop.procesor = request.POST.get('procesor')
        # Adaugă aici și alte câmpuri relevante

        laptop.save()
        return redirect('/admin-dashboard/cautare_laptop/')  # Redirect după salvare

    return render(request, 'shop/edit-laptop.html', {'laptop': laptop})

# shop/views.py
from django.shortcuts import render, redirect
from .forms import TabletaForm

def adauga_tableta(request):
    if request.method == 'POST':
        form = TabletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adauga_tableta')  # sau pagina de listare
    else:
        form = TabletaForm()
    return render(request, 'shop/adauga_tableta.html', {'form': form})

from .models import Tableta
def cautare_tableta(request):
    tablete = None
    marca = None

    if request.method == 'POST':
        marca = request.POST.get('marca', '').strip()
        if marca:
            # Căutăm atât în Brand cât și în Model
            tablete = Tableta.objects.filter(Brand__icontains=marca) | Tableta.objects.filter(Model__icontains=marca)

    return render(request, 'shop/cautare_tableta.html', {
        'tablete': tablete,
        'marca': marca
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Tableta

def edit_tableta(request, serietableta):
    tableta = get_object_or_404(Tableta, SerieTableta=serietableta)

    if request.method == 'POST':
        tableta.SistemOperare = request.POST.get('SistemOperare')
        tableta.Brand = request.POST.get('Brand')
        tableta.Model = request.POST.get('Model')
        tableta.CapacitateRAM = request.POST.get('CapacitateRAM')
        tableta.CapacitateMemorie = request.POST.get('CapacitateMemorie')
        tableta.Culoare = request.POST.get('Culoare')
        tableta.Lungime = request.POST.get('Lungime')
        tableta.Latime = request.POST.get('Latime')
        tableta.UnitatiMasura = request.POST.get('UnitatiMasura')
        tableta.Grosime = request.POST.get('Grosime')
        tableta.Greutate = request.POST.get('Greutate')
        tableta.CapacitateAcumulator = request.POST.get('CapacitateAcumulator')
        tableta.Rezolutie = request.POST.get('Rezolutie')
        tableta.Diagonala = request.POST.get('Diagonala')
        tableta.Conectivitate = request.POST.get('Conectivitate')
        tableta.ModelProcesor = request.POST.get('ModelProcesor')
        tableta.pret = request.POST.get('pret')
        tableta.Disponibilitate = request.POST.get('Disponibilitate')
        tableta.OptiuneLivrare = request.POST.get('OptiuneLivrare')

        tableta.save()
        return redirect('/admin-dashboard/cautare_tableta/')

    return render(request, 'shop/edit_tableta.html', {'tableta': tableta})

def delete_tableta(request):
    if request.method == "POST":
        serial = request.POST.get("SerieTableta")
        tableta = get_object_or_404(Tableta, SerieTableta=serial)
        tableta.delete()
        return redirect('/admin-dashboard/cautare_tableta/')
    else:
        return redirect('/admin-dashboard/cautare_tableta/')