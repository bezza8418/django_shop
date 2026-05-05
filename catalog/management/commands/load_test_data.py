import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур'

    def handle(self, *args, **options):
        # Путь к фикстурам
        fixtures_dir = 'catalog/fixtures'
        categories_fixture = os.path.join(fixtures_dir, 'categories.json')
        products_fixture = os.path.join(fixtures_dir, 'products.json')

        # Проверяем, есть ли фикстуры
        if not os.path.exists(categories_fixture):
            self.stdout.write(self.style.ERROR('❌ Файл categories.json не найден!'))
            return

        if not os.path.exists(products_fixture):
            self.stdout.write(self.style.ERROR('❌ Файл products.json не найден!'))
            return

        # Спрашиваем подтверждение
        self.stdout.write('⚠️  Будут удалены все существующие категории и продукты!')
        confirm = input('Вы уверены? (y/n): ')

        if confirm.lower() != 'y':
            self.stdout.write('❌ Операция отменена.')
            return

        # Очищаем существующие данные
        deleted_categories_count = Category.objects.all().delete()
        self.stdout.write(f'✅ Удалено объектов: {deleted_categories_count[0]}')

        # Загружаем новые данные из фикстур
        call_command('loaddata', categories_fixture)
        call_command('loaddata', products_fixture)

        self.stdout.write(self.style.SUCCESS('🎉 Тестовые данные успешно загружены!'))
