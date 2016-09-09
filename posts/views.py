from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from forms import PostForm

# Create your views here.
from posts.models import Post

def post_create(request):
    form = PostForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    
    #if request.method == "POST":
    #   print request.POST.get("title")
    
    context = {
        "form": form
    }
    
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    #queryset = Post.objects.filter(id=6).values()
    queryset = get_object_or_404(Post,id=id)
        
    content = {
        "instance": queryset, 
    }
    
    return render(request, "post_detail.html", content)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")


def post_list(request):
    queryset = Post.objects.all()
        
    content = {
        "queryset": queryset, 
        "content": "List Content Auth!"
    }
    

    return render(request, "index.html", content)
