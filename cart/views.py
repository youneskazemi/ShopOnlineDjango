from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from shop.models import Product
from .forms import CartAddForm
from django.views.decorators.http import require_POST
from django.contrib import messages


def detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'])
        messages.success(request, f'{cd["quantity"]} {product.name} added successfully to your cart', 'success')
    return redirect("shop:product_detail", product.slug)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:detail")
