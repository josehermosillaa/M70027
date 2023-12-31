from django.shortcuts import render, HttpResponseRedirect
from .models import Post
from django.template.defaultfilters import slugify
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }

    return render(request, "blogsite/index.html", context)

def agregar(request):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            content=request.POST["content"],
            author=request.POST["author"]
            )
        return HttpResponseRedirect("/post/")
    elif request.method == "GET":
        form = PostForm()
        context = {"form":form}
        return render(request,"blogsite/agregar.html", context)

def eliminar(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect("/post/")

def actualizar(request, id):
    print(f"{request.POST}")
    if request.method == "POST":
        Post.objects.filter(id=id).update(
            title=request.POST["title"],
            content=request.POST["content"],
            author=request.POST["author"],
            slug=slugify(request.POST["title"])
            )

        return HttpResponseRedirect("/post/")
    elif request.method == "GET":
        post = Post.objects.get(id=id)
        context = {"post":post}
        return render(request,"blogsite/actualizar.html", context)