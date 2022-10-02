from socket import fromshare
from django import forms

class FormularioArticulo(forms.Form):

    public_options = [
        (0, 'No'),
        (1, 'Si')
    ]

    title = forms.CharField(
        label = "Titulo",
    )
    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea,
    )
    public = forms.TypedChoiceField(
        choices = public_options
    )