from django.urls import path 

from .views import home

urlpatterns = [
    path('', home, name='index'),
    #This is another 
    '''
     i have been trying to make some changes sincee all this while.
    '''
]