from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.
def view_list(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")