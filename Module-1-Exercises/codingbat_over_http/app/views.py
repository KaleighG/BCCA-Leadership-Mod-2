from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
# Create your views here.

def nearHundred(request: HttpRequest,  n: int) -> HttpResponse:
  return HttpResponse(abs(100 - n) <= 10 or abs(200 - n) <= 10)  

def stringSplosion(request: HttpRequest, string: str) -> HttpResponse:
    result = ""
    for i in range(len(string)):
        result += string[:i+1]
    return HttpResponse(result)

def catDog(request: HttpRequest, string: str) -> HttpResponse:
    cat_count = string.count("cat")
    dog_count = string.count("dog")
    return HttpResponse(cat_count == dog_count)

def loneSum(request: HttpRequest, n1: int, n2: int, n3: int) -> HttpResponse:
     if n1 == n2 == n3:
        return HttpResponse(0)
     elif n1 == n2:
        return HttpResponse(n3)
     elif n1 == n3:
        return HttpResponse(n2)
     elif n2 == n3:
        return HttpResponse(n1)
     else:
        return HttpResponse(n1 + n2 + n3)