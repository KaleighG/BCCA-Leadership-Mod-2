from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass 
from typing import List

@dataclass
class Team:
    name: str
    description: str
    member: List[str]




# Create your views here.
def view_list(request: HttpRequest) -> HttpResponse:
    context = {'teams':[
    Team(
        'Community',
        'Provides a good environment and the occasional fun time for the whole school.',
        ['Jordan','Joby','Aj','Micah','Caleb'] ),
    Team(
        'Documentation',
        'Documents events at bcca ,with access to the media accounts and social pages.',
        ['Conner','Kaleigh','Blair','Mina','Jay','Joshua'] ),
    Team(
        'Management',
        'Hands out work loads and makes efforts on maintaining the student body.',
        ['Owen','Jeremiah','Nick','Ab','Abigail'] ),
    Team(
        'Procurement',
        'Accumulates supply for things such as lunch, building maintenance, and events. ',
        ['Kayleah','Adrian','Bryce','Big John','Blaine', 'Wyatt'] )
    ]}

    
    return render(request, "index.html", context)

def view_details(request: HttpResponse, team: str) -> HttpResponse:
    if team == 'community':
        context = {'teams':
    Team(
        'Community',
        'Provides a good environment and the occasional fun time for the whole school.',
        ['Jordan','Joby','Aj','Micah','Caleb'] )}  
    elif team == "management":
        context = {'teams':
    Team('Management',
        'Hands out work loads and makes efforts on maintaining the student body.',
        ['Owen','Jeremiah','Nick','Ab','Abigail'] )}
    elif team == "documentation":
        context = {'teams': 
        Team(
        'Documentation',
        'Documents events at bcca ,with access to the media accounts and social pages.',
        ['Conner','Kaleigh','Blair','Mina','Jay','Joshua'] )}
    elif team == 'procurement':
        context = {'teams':
        Team(
        'Procurement',
        'Accumulates supply for things such as lunch, building maintenance, and events. ',
        ['Kayleah','Adrian','Bryce','Big John','Blaine', 'Wyatt'] )}

    return render(request, "details.html", context )






