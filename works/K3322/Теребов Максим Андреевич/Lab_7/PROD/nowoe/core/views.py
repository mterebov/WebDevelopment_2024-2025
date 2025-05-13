from django.shortcuts import render
from .models import Product
from .forms import OrderForm

def index(request):
    products = Product.objects.all()
    return render(request, 'core/index.html', {'products': products})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/contact.html', {'success': True})
    else:
        form = OrderForm()
    
    return render(request, 'core/contact.html', {'form': form})