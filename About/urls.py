from django.urls import path
from About import views

urlpatterns = [
   path('about/', views.myAbout, name='about'),
]
