from django import forms
from .models import Prenda, Categoria


class PrendaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        label="Categoría",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'categoria-select',
            'title': 'Selecciona una categoría para filtrar las opciones disponibles',
        })
    )

    class Meta:
        model = Prenda
        fields = ['codigo', 'nombre', 'descripcion', 'talla', 'precio', 'estado', 'imagen']
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: PRD-001',
                'title': 'Código único para la prenda (ej: PRD-001)'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'title': 'Escribe el nombre de la prenda, por ejemplo: Camiseta blanca',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'title': 'Agrega una descripción breve: tela, estilo, etc.',
            }),
            'talla': forms.TextInput(attrs={
                'class': 'form-control',
                'title': 'Indica la talla: S, M, L, etc.',
            }),
            'precio': forms.TextInput(attrs={
                'class': 'form-control',
                'title': 'Establece el precio en pesos (ej: $20000)',
                'inputmode': 'numeric',
                'id': 'precio-input'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'form-control',
                'title': 'Ej: Como nueva, Usada en buen estado...',
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'title': 'Selecciona una imagen de la prenda',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        qs = Prenda.objects.filter(codigo=codigo)

        # Excluir la prenda actual si estamos editando
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("⚠️ Ya existe una prenda con este código.")

        return codigo