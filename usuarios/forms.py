from django import forms

class LoginForm(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
# código omitido
    
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
    widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )


class CadastroForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome'
            }
        )
    )

    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu e-mail'
            }
        )
    )

    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
    widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

    senha_2 = forms.CharField(
        label='Confirme sua senha',
        required=True,
        max_length=70,
    widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente'
            }
        )
    )