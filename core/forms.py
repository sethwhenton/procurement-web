# core/forms.py

from django import forms
from .models import Item, CustomUser, Department, Budget, Company

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'department', 'budget']

    def __init__(self, *args, **kwargs):
        company_id = kwargs.pop('company_id', None)
        super(UserForm, self).__init__(*args, **kwargs)
        if company_id:
            self.fields['department'].queryset = Department.objects.filter(company_id=company_id)
            self.fields['budget'].queryset = Budget.objects.filter(company_id=company_id)
        else:
            self.fields['department'].queryset = Department.objects.none()
            self.fields['budget'].queryset = Budget.objects.none()

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['classification', 'amount']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']
