from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создаёт группу "Модератор продуктов" и назначает права'

    def handle(self, *args, **options):
        # Получаем или создаём группу
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Получаем content type для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Права для группы
        permissions = [
            'can_unpublish_product',   # кастомное право
            'delete_product',           # право на удаление
        ]

        for codename in permissions:
            try:
                permission = Permission.objects.get(
                    codename=codename,
                    content_type=content_type
                )
                group.permissions.add(permission)
                self.stdout.write(f'✅ Добавлено право: {codename}')
            except Permission.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'⚠️ Право {codename} не найдено'))

        group.save()
        self.stdout.write(self.style.SUCCESS('🎉 Группа "Модератор продуктов" создана и настроена!'))
