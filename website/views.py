from django.shortcuts import render
from .models import Post, PostForm


# Create your views here.
def publicaciones(request):
    publicaciones = Post.objects.all()
    form = PostForm()
    editing = False
    id = None
    if request.method == "POST":
        print(request.POST)
        if "eliminar" in request.POST:
            Post.objects.get(id=request.POST.get("id")).delete()
        elif "editar" in request.POST:
            post = Post.objects.get(id=request.POST.get("id"))
            form = PostForm(instance=post)
            editing = True
            id = post.id
        elif "guardar" in request.POST:
            form = PostForm(request.POST)
            if form.is_valid():
                if request.POST.get("editing") == "True":
                    post = Post.objects.get(id=request.POST.get("id"))
                    post.titulo = form.cleaned_data["titulo"]
                    post.contenido = form.cleaned_data["contenido"]
                    post.save()
                    editing = False
                    form = PostForm()
                else:
                    form.save()
                    form = PostForm()
    return render(
        request,
        "website/publicaciones.html",
        {
            "publicaciones": publicaciones,
            "formulario": form,
            "editing": editing,
            "id": id,
        },
    )
