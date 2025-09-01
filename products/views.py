from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

def home(request):
    products = Product.objects.all()

    # Search
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(name__icontains=search_query) | products.filter(brand__icontains=search_query)

    # Filters
    price_min = request.GET.get('price__gte')
    price_max = request.GET.get('price__lte')
    is_available = request.GET.get('is_available')

    if price_min:
        products = products.filter(price__gte=price_min)
    if price_max:
        products = products.filter(price__lte=price_max)
    if is_available in ['True', 'False']:
        products = products.filter(is_available=is_available == 'True')

    paginator = Paginator(products, 10)  # 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/home.html', {'page_obj': page_obj})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})
