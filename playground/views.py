from django.shortcuts import render
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(collection__id=3)

    return render(request, "hello.html", {"name": "Guest", 'products': list(queryset)})
