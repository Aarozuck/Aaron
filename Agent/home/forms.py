from django import forms
from .models import Teacher, Customer


class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'phone_number', 'abilities', 'subjects', 'price_per_hour', 'schools_taught']


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'phone_number']


class LoginForm(forms.Form):
    full_name = forms.CharField()
    phone_number = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get('full_name')
        phone_number = cleaned_data.get('phone_number')

        try:
            Teacher.objects.get(full_name=full_name, phone_number=phone_number)
        except Teacher.DoesNotExist:
            try:
                Customer.objects.get(full_name=full_name, phone_number=phone_number)
            except Customer.DoesNotExist:
                raise forms.ValidationError('Invalid full name or phone number')