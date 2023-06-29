from django.core.files.images import get_image_dimensions
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    MAX_IMAGE_SIZE = (720, 720)  # Tamaño máximo permitido para la imagen

    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'imagen', 'precio', 'stock')

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')

        if imagen:
            width, height = get_image_dimensions(imagen)
            if width > self.MAX_IMAGE_SIZE[0] or height > self.MAX_IMAGE_SIZE[1]:
                raise forms.ValidationError(
                    f"La imagen no puede ser mayor a {self.MAX_IMAGE_SIZE[0]}x{self.MAX_IMAGE_SIZE[1]} píxeles."
                )

        return imagen

