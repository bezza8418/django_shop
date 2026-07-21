from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Product
from .forms import ProductForm


class HomeView(ListView):
    """Главная страница со списком товаров и пагинацией"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    paginate_by = 6


class ProductDetailView(DetailView):
    """Детальная страница товара"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    """Добавление нового товара"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        messages.success(self.request, 'Товар успешно добавлен!')
        return super().form_valid(form)


class ContactsView(TemplateView):
    """Страница контактов с формой обратной связи"""
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        print(f"\n📬 Получено сообщение от {name} ({email}):")
        print(f"Сообщение: {message}\n")

        return render(request, self.template_name, {'message_sent': True})
