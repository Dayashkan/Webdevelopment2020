from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Product, Category


def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(product.to_json())


def categories_list(request):
    categories = Category.objects.all()
    category_json = [category.to_json() for category in categories]
    return JsonResponse(category_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())


def products_by_category(request, id):
    products = Category.objects.get(id=id)
    all_products = Product.objects.all()
    for p in all_products:
        if p.id == products.id:
            return JsonResponse(products.to_json())
# Create your views here.
