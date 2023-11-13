from django.urls import path
from . import views

urlpatterns=[
    path('index.html',views.index,name='index.html'),
    path('login.html',views.login,name='login.html'),
    path('formulario.html',views.formulario,name='formulario.html'),
    path('admin.html',views.admin,name='admin.html'),
    path('adminlist.html',views.adminlist,name='adminlist.html'),
    path('adminsearch.html',views.adminsearch,name='adminsearch.html'),
    path('book.html',views.book,name='book.html'),
    path('bookconfig.html',views.adminsearch,name='bookconfig.html'),
    path('bookinfo.html',views.bookinfo,name='bookinfo.html'),
    path('catalog.html',views.catalog,name='catalog.html'),
    path('category.html',views.category,name='category.html'),
    path('categorylist.html',views.categorylist,name='categorylist.html'),
    path('client.html',views.client,name='client.html'),
    path('clientlist.html',views.clientlist,name='clientlist.html'),
    path('clientsearch.html',views.clientsearch,name='clientsearch.html'),
    path('company.html',views.company,name='company'),
    path('companylist.html',views.companylist,name='companylist.html'),
    path('home.html',views.home,name='home'),
    path('myaccount.html',views.myaccount,name='myaccount.html'),
    path('mydata.html',views.mydata,name='mydata.html'),
    path('provider.html',views.provider,name='provider.html'),
    path('providerlist.html',views.providerlist,name='providerlist.html'),
    path('search.html',views.search,name='search.html'),


]