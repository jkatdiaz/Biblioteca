from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'paginas/index.html')

def login(request):
    return render(request,'paginas/login.html')

def formulario(request):
    return render(request,'paginas/formulario.html')

def admin(request):
    return render(request,'paginas/admin.html')

def adminlist(request):
    return render(request,'paginas/adminlist.html')

def adminsearch(request):
    return render(request,'paginas/adminsearch.html')

def book(request):
    return render(request,'paginas/book.html')

def bookinfo(request):
    return render(request,'paginas/bookinfo.html')

def bookconfig(request):
    return render(request,'paginas/bookconfig.html')    

def catalog(request):
    return render(request,'paginas/catalog.html')    

def category(request):
    return render(request,'paginas/category.html')

def categorylist(request):
    return render(request,'paginas/categorylist.html')

def client(request):
    return render(request,'paginas/client.html')

def clientlist(request):
    return render(request,'paginas/clientlist.html')

def clientsearch(request):
    return render(request,'paginas/clientsearch.html')

def company(request):
    return render(request,'paginas/company.html')

def companylist(request):
    return render(request,'paginas/companylist.html')

def home(request):
    return render(request,'paginas/home.html')

def myaccount(request):
    return render(request,'paginas/myaccount.html')

def mydata(request):
    return render(request,'paginas/mydata.html')

def provider(request):
    return render(request,'paginas/provider.html')

def providerlist(request):
    return render(request,'paginas/providerlist.html')

def search(request):
    return render(request,'paginas/search.html')    