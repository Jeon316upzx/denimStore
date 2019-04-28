from django.shortcuts import render
from Collection.models import Products
from Collection.forms import productform

# Create your views here.

def myCollection(request):
    myproducts = Products.objects.all()
    return render(request, 'Collection/products.html',{ 'myproducts': myproducts })

def c_detail(request,pk):
    if request.method == 'POST':
        form = productform(request.POST,request.FILES)
    else:
        form = productform()
        myproduct = Products.objects.get(pk=pk)
    return render(request, 'Collection/details.html',{'myproduct': myproduct,'form': form })
