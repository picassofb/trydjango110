from urllib.parse import quote_plus
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, Http404
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from posts.models import Post


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    elif request.POST:
        messages.error(request, "Error on create")
    context = {
        "form": form
    }

    return render(request, "post_form.html", context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)

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


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
    }
    return render(request, "post_detail.html", context)


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Post Deleted!")
    return redirect("posts:list")


def post_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 3)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
        
    content = {
        "queryset": queryset, 
        "content": "List Content Auth!",
        "page_request_var": page_request_var
    }
    return render(request, "post_list.html", content)

