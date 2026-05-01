from django.shortcuts import render

def home(request):
    """Контроллер для главной страницы"""
    return render(request, 'catalog/home.html')


def contacts(request):
    """Контроллер для страницы контактов с обработкой формы"""
    message_sent = False

    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        print(f"\n📬 Получено сообщение от {name} ({email}):")
        print(f"Сообщение: {message}\n")

        # Устанавливаем флаг, что сообщение отправлено
        message_sent = True

    return render(request, 'catalog/contacts.html', {'message_sent': message_sent})
