from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm, Profile
from .forms import ContactFormForm, ContactModelForm, ProfileForm, UserForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def indice(req):
    flanes_all = Flan.objects.all()
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {"flanes_publicos": flanes_publicos,
            "flanes_all": flanes_all,
            }
    return render(req, 'index.html', context)


def acerca(req):
    contex = {
        "data": "Acerca de nosotros"
    }
    return render(req, 'about.html', contex)

@login_required
def bienvenido(req):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(req, 'welcome.html', {"flanes_privados": flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST) 
        if form.is_valid():
            ContactForm.objects.create(**form.cleaned_data) 
            return HttpResponseRedirect('/exito')
    else: 
        form = ContactModelForm()    
    return render(request, 'contactus.html', {'form':form})

def exclusivos(req):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(req, 'exclusivos.html', {"flanes_privados": flanes_privados})

def exito(request):
    return render(request, 'success.html', {})

def detalle(request, flan_uuid):
    flan=Flan.objects.get(flan_uuid=flan_uuid)
    return render(request, 'detalle.html', {'flan':flan})

@login_required
def profile_view(request):
    # Verificar que el User tiene un Perfil 
    user_id = request.user.id 
    
    user = request.user
    #* User de no tener un Profile, crea la relación
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
        profile = Profile.objects.get(user_id=user_id)
        print(f'user profile get -> {profile.__dict__}')
        
    #* ARMADO POST - crea (guarda en la tabla) - y redirect
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Redirigir a la misma página después de guardar
            return redirect('/profile_exito')
    #* GET FORM - Creamos los forms con los datos de la DB de ese user
    else: 
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def profile_exito(request):
    return render(request, 'profile_exito.html', {})

def profile_e(request):
    return render(request, 'profile_e.html', {})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #* Se guarda el user en la DB
            login(request, user) #* Se logea
            return redirect('profile')  # Redirige a la vista de perfil u otra vista
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


