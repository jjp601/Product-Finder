from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from.models import Product
from django.utils import timezone

# Create your views here.
def index(request):
    products = Product.objects
    return render(request, 'products/index.html', {'products': products})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['description'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.name = request.POST['name']
            product.description = request.POST['description']
            product.url = request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.founder = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'products/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})


@login_required(login_url="/accounts/register")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes += 1
        product.save()
        return redirect('/products/' + str(product.id))

