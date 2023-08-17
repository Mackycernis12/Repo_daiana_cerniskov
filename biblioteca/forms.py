from django import forms

class Users_form(forms.Form):
    usuario = forms.CharField(max_length=60)
    clave = forms.IntegerField()


class cliente_form(forms.Form):
    nombre = forms.CharField(max_length=60)
    email = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)

class libros_form(forms.Form):
    nombre = forms.CharField(max_length=150)
    Editorial = forms.CharField(max_length=100)
    año_publicacion = forms.IntegerField()

class BusquedaForm(forms.Form):
    nombre = forms.CharField(label='Buscar por nombre', max_length=100)
