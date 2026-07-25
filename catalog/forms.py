from django import forms
from .models import Product

# Запрещённые слова (список вынесен в константу)
FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Описание товара'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена в рублях'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name_lower = name.lower()
        for word in FORBIDDEN_WORDS:
            if word in name_lower:
                raise forms.ValidationError(
                    f'Название содержит запрещённое слово: "{word}".'
                )
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        desc_lower = description.lower()
        for word in FORBIDDEN_WORDS:
            if word in desc_lower:
                raise forms.ValidationError(
                    f'Описание содержит запрещённое слово: "{word}".'
                )
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError(
                'Цена не может быть отрицательной. Пожалуйста, введите корректную цену.'
            )
        return price

