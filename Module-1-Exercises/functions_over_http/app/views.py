from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.
def HeyYou(request: HttpRequest, item: str) -> HttpResponse:
    return HttpResponse(f'Hey, {item}!')

def AgeIn(request: HttpRequest, end: int, year: int) -> HttpResponse:
    return HttpResponse (f'{float(end) - float(year):.0f}')

def OrderTotal(request: HttpRequest, burgers: int, fries: int, drinks: int) -> HttpResponse:
    return HttpResponse (f'Order Total: ${(int(burgers) * 4.5) + (int(fries) * 1.5) + (int(drinks) * 1):.1f}')