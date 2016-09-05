from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def post_create(request):
    return HttpResponse("<h1>Create</h1>")


def post_detail(request):
    return HttpResponse("<h1>Detail</h1>")


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")


def post_list(request):
    if request.user.is_authenticated():
        content = {
            "title": "List Content Auth"
        }
    else:
        content = {
            "title": "List Content Auth!"
        }

    return render(request, "index.html", content)
