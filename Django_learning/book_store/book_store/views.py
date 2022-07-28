
from django.shortcuts import  HttpResponse


def index(request):
    power = request.GET['number']
    power = int(power)**2
    print(power)
    # fname = request.GET['fname']
    # lname = request.GET['lname']
    # return  HttpResponse (f'<h1>hello {fname} {lname} </h1>')
    return HttpResponse(f'<h1>{power}</h1>')

# def comand(request):
#     return HttpResponse('<h1>-------------</h1>') 

# def require(request):
#     return HttpResponse('<h1>rama singh</h1>')       