from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from .models import Product
from .forms import ProductForm
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class HomeView(ListView):
    """Главная страница со списком товаров и пагинацией"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.all()


@method_decorator(cache_page(60 * 15), name='dispatch')  # кеш на 15 минут
class ProductDetailView(LoginRequiredMixin, DetailView):
    """Детальная страница товара (только для авторизованных)"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Добавление нового товара (только для авторизованных)"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Товар успешно добавлен!')
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование товара (только для владельца или модератора)"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user and not request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied('У вас нет прав на редактирование этого товара.')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Товар успешно обновлён!')
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление товара (только для владельца или модератора)"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user and not request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied('У вас нет прав на удаление этого товара.')
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Товар успешно удалён!')
        return super().delete(request, *args, **kwargs)


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


@permission_required('catalog.can_unpublish_product')
def unpublish_product(request, pk):
    """Снятие продукта с публикации (только для модераторов)"""
    product = get_object_or_404(Product, pk=pk)
    product.status = 'draft'
    product.save()
    messages.success(request, f'Продукт "{product.name}" снят с публикации.')
    return redirect('catalog:product_detail', pk=pk)
