from django import forms
from .models import Partido, Candidato, Votacion

class FormPartido(forms.ModelForm):

    class Meta:
        model = Partido
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder': 'Nombre del partido Político',
                    }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe una descripción'
                }
            ),
        }

class FormFiltrosPartido(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}))
    descripcion = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Descripcion', 'class': 'form-control'}))


class FormCandidato(forms.ModelForm):

    class Meta:
        model = Candidato
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder': 'Nombre',
                    }
            ),
            'apellido_pat': forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder': 'Apellido paterno',
                    }
            ),
            'apellido_mat': forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder': 'Apellido materno',
                    }
            ),
            'partido': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }

class FormFiltrosCandidato(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}))
    apellido_pat = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Apellido paterno', 'class': 'form-control'}))
    apellido_mat = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Apellido materno', 'class': 'form-control'}))
    partido = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Partido', 'class': 'form-control'}))


class FormVotacion(forms.ModelForm):

    class Meta:
        model = Votacion
        fields = '__all__'


        widgets = {
            'candidato': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'fecha_hora': forms.DateInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }