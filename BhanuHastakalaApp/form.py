from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =["title", "slug", "category", "image", "market_price", "selling_price", "description", "warrenty", "return_policy"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter The Product Name..eg: Cup Board"}),

            "slug": forms.TextInput(attrs={
                "placeholder": "eg: cup-board"}),

            "description": forms.TextInput(attrs={
                "placeholder": "Description........"}),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"}),



        }