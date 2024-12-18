
from django.shortcuts import render, redirect

from usuarios.forms import LoginForm, CadastroForm

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login(request):
        form = LoginForm()

        if request.method == "POST":
                form = LoginForm(request.POST)

                if form.is_valid():     
                        nome = form['nome_login'].value()
                        senha=form["senha"].value()


                usuario = auth.authenticate(
                        request,
                        username=nome, 
                        password=senha)
                
                if usuario is not None:
                        auth.login(request, usuario)
                        messages.success(request, f"{nome} Logado(a) realizado com sucesso")
                        return redirect("index")
                else:
                        messages.error(request, "Usuário ou senha inválidos")
                        return redirect("login")

        return render(request, "usuarios/login.html", {"form": form})


def cadastro(request):

        form = CadastroForm()

        if request.method == "POST":
                form = CadastroForm(request.POST)
                
                if form.is_valid():
                        if form ["senha_1"].value() != form ["senha_2"].value():
                                messages.error(request, "As senhas não conferem")
                                form.add_error("senha_2", "As senhas não conferem")
                                return redirect("cadastro")

                        nome =form["nome"].value()
                        email = form["email"].value()
                        senha = form["senha_1"].value()

                        if User.objects.filter(username=nome).exists():
                                messages.error(request, "Usuário já cadastrado")
                                return redirect("cadastro")
                        
                        usuario = User.objects.create_user(
                                username = nome, 
                                email = email, 
                                password =senha
                                )
                        usuario.save()
                        messages.success(request, f"{nome} cadastrado com sucesso")
                        return redirect("login")

        return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
        auth.logout(request)
        messages.success(request, "Deslogado com sucesso")
        return redirect("login")

