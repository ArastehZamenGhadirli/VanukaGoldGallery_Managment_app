from django.urls import path

#from .views import get_blackboard,add_content,delete_content,clear_blackboard


#urlpatterns = [
#    path('products/' ,  )
#  
#]
#

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

