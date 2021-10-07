from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


@login_required
def detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/detail.html', {'order': order})


@login_required
def create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    cart.clear()
    return redirect("orders:orders_detail", order.id)
