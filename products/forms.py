from django import forms
from .models import ProductComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['text']  # فیلدهایی که می‌خواهید در فرم نمایش داده شوند
        # text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'نظر شما', 'rows': 5}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # اضافه کردن ویژگی‌های بیشتر به فیلدهای فرم، اگر نیاز دارید
