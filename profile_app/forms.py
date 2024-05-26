from django import forms
from accounts.models import User,Address

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'national_code','email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'national_code': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماره همراه',
            'national_code': 'کد ملی',
            'email': 'ایمیل',
        }
        help_texts = {
            'email': 'info@gmail.com',
        }

class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address', 'postal_code', 'emergency_call', 'receiver','user']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_call': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'address': 'آدرس',
            'postal_code': 'کد پستی',
            'emergency_call': 'شماره تماس',
            'receiver': 'گیرنده',
        }