from django.shortcuts import render, get_object_or_404, redirect

from galeria.models import Fotografia

from django.contrib import messages

from galeria.forms import FotografiaForm

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar essa página.")
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request,foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar essa página.")
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
   
    return render(request, 'galeria/index.html', {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar essa página.")
        return redirect ('login')

    form = FotografiaForm
    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES)
        if form.is_valid():
            fotografia = form.save(commit=False)
            fotografia.usuario = request.user
            fotografia.save()
            messages.success(request, "Imagem cadastrada com sucesso!")
            return redirect('nova_imagem')
        else:
            messages.error(request, "Erro ao cadastrar a imagem.")
        
    return render(request, 'galeria/nova_imagem.html', {'form': form})
    


def editar_imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, id=foto_id)
    form = FotografiaForm(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, "Imagem editada com sucesso!")
            return redirect('editar_imagem', foto_id=foto_id)
        else:
            messages.error(request, "Erro ao editar a imagem.")

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id, 'fotografia': fotografia})


def deletar_imagem(request,foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, "Imagem deletada com sucesso!")
    return redirect('index')

# views.py
def filtro(request, categoria):
    # Normalizar a categoria para evitar problemas com case sensitivity e espaços
    categoria = categoria.strip().upper()

    fotografias = Fotografia.objects.filter(publicada=True, categoria=categoria).order_by("data_fotografia")

    return render(request, 'galeria/index.html', {"cards": fotografias})