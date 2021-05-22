from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import *
from .forms import *
from .filters import OrderFilter

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {
        'products': products,
    })

def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    total_orders = orders.count()

    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders,
        'myfilter': my_filter,
        }
    return render(request, 'accounts/customer.html', context) 

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('accounts:home')

    context = {
        'formset': formset,
    }
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('accounts:home')
    context = {
        'form': form,
    }
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    item = Order.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('accounts:home')
    context = {
        'item': item,
    }
    return render(request, 'accounts/delete.html', context)