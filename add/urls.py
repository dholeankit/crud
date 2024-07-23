from operator import index
from django.urls import path 
from .views import *
from .views import deleteEmployee
from .views import updateEmployee 

urlpatterns = [
    # path('',index,name='addd'),
    path('',employee,name='crud'),
    path("delete/<int:id>",deleteEmployee,name="deleteEmploye"),
    path("update/<int:id>",updateEmployee,name="updateEmploye"),
]