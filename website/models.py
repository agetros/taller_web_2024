from django.db import models
from django.forms import ModelForm, TextInput, Textarea


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido"]
        widgets = {
            "titulo": TextInput(attrs={"class": "form-control"}),
            "contenido": Textarea(attrs={"class": "form-control"}),
        }
