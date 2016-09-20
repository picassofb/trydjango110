from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from django.contrib import messages

# Create your views here.
from posts.models import Post


def post_create(request):
    form = PostForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    elif request.POST:
        messages.error(request, "Error on create")
    context = {
        "form": form
    }

    return render(request, "post_form.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "instance": instance,
        "form": form
    }
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post Deleted!")
    return redirect("posts:list")


def post_list(request):
    queryset = Post.objects.all()
        
    content = {
        "queryset": queryset, 
        "content": "List Content Auth!"
    }
    return render(request, "post_list.html", content)
