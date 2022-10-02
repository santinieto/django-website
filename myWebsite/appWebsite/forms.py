from socket import fromshare
from django import forms

class FormularioArticulo(forms.Form):

    public_options = [
        (0, 'No'),
        (1, 'Si')
    ]

    title = forms.CharField(
        label = "Titulo",
        max_length = 20, # Cantidad maxima de caracteres
        required = False, # Obliga o no a llenar este campo
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'Titulo del articulo',
            }
        ),
    )
    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea(
            attrs = {
                'placeholder' : 'Contenido del articulo',
            }
        ),
    )
    public = forms.TypedChoiceField(
        choices = public_options
    )

    # Como modificar los atributos del formulario
    content.widget.attrs.update({
        'placeholder' : 'Nuevo contenido del articulo'
    })