from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem, Coupon
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .forms import CouponForm
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib import messages


@login_required
def detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = CouponForm()
    return render(request, 'orders/detail.html', {'order': order, 'form': form})


@login_required
def create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    cart.clear()
    return redirect("orders:orders_detail", order.id)


@require_POST
def coupon_apply(request, order_id):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)

            order = Order.objects.get(id=order_id)
            order.discount = coupon.discount
            order.save()
            messages.warning(request, "coupon added successfully", 'success')
            return redirect('orders:orders_detail', order_id)
        except Coupon.DoesNotExist:
            messages.warning(request, "invalid coupon!", 'danger')
            return redirect('orders:orders_detail', order_id)
