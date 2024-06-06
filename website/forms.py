from django.forms import ModelForm, TextInput, Textarea
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category"]
