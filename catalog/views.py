from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    """Контроллер для главной страницы со списком товаров"""
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})


def contacts(request):
    """Контроллер для страницы контактов с обработкой формы"""
    message_sent = False

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        print(f"\n📬 Получено сообщение от {name} ({email}):")
        print(f"Сообщение: {message}\n")

        message_sent = True

    return render(request, 'catalog/contacts.html', {'message_sent': message_sent})


def product_detail(request, pk):
    """Контроллер для детальной страницы товара"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def add_product(request):
    """Контроллер для добавления нового товара"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Товар успешно добавлен!')
            return redirect('catalog:home')
    else:
        form = ProductForm()

    return render(request, 'catalog/add_product.html', {'form': form})


def home(request):
    """Контроллер для главной страницы с пагинацией"""
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 6)  # 6 товаров на страницу

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'catalog/home.html', {'products': products})
