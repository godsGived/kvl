from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def health_check(request):
    return JsonResponse({'status': 'ok'})

def product_list(request):
    items = Product.objects.all().order_by('-created_at')
    return render(request, 'products/product_list.html', {'items': items})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'item': None})

def product_update(request, pk):
    item = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=item)
    return render(request, 'products/product_form.html', {'form': form, 'item': item})

def product_delete(request, pk):
    item = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'item': item})