from django.urls import path
from Collection import views

app_name = 'Collections'
urlpatterns = [
    path('collection/', views.myCollection, name='collection'),
    path('collection/<uuid:pk>', views.c_detail, name='product-detail'),
]
