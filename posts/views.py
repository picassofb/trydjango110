from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from posts.models import Post

def post_create(request):
    return HttpResponse("<h1>Create</h1>")


def post_detail(request):
    #queryset = Post.objects.filter(id=6).values()
    queryset = get_object_or_404(Post,id=3)
        
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
