from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from BhanuHastakalaApp.models import Product, Category
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from .form import ProductForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin





class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_index = Product.objects.all().order_by('-id')[:6]
        context['product_index'] = product_index
        return context

class AllProduct(TemplateView):
    template_name = 'bhanuhastakalaapp/allproducts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_product = Product.objects.all().order_by("-id")
        paginator = Paginator(all_product, 8)
        page_number = self.request.GET.get('page')
        product_list = paginator.get_page(page_number)
        context['product_list'] = product_list
        return context


class Bed(TemplateView):
    template_name = 'bhanuhastakalaapp/bed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_bed = Category.objects.filter(title='Bed')
        paginator = Paginator(all_bed, 3)
        page_number = self.request.GET.get('page')
        bed_list = paginator.get_page(page_number)
        context['bed_list'] = bed_list
        return context

class Dinning(TemplateView):
    template_name = 'bhanuhastakalaapp/dinningtable.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dinning = Category.objects.filter(title='Dinning Table/Table')
        context["dinning"] = dinning
        return context

class Sofa(TemplateView):
    template_name = 'bhanuhastakalaapp/sofa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sofa = Category.objects.filter(title='Sofa')
        context["sofa"] = sofa
        return context

class Cup(TemplateView):
    template_name = 'bhanuhastakalaapp/cup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cup = Category.objects.filter(title='Cup Board')
        context["cup"] = cup
        return context




class ProductDetails(TemplateView):
    template_name = 'bhanuhastakalaapp/ProductDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        product = Product.objects.get(slug=url_slug)
        product.review_count += 1
        product.save()
        context['product'] = product
        return context


class SearchView(TemplateView):
    template_name = 'bhanuhastakalaapp/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("keyword")
        result = Product.objects.filter(Q(title__icontains=kw) | Q(description__icontains=kw) | Q(selling_price__icontains=kw))
        context["result"]= result
        return context


class about(TemplateView):
    template_name = 'bhanuhastakalaapp/about.html'

# class contact(TemplateView):
#     template_name = 'bhanuhastakalaapp/contact.html'

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(subject, message, email, ['bhanuhastakala@gmail.com'])

        return render(request, 'bhanuhastakalaapp/contact.html', {'name': name})
    else:
        return render(request, 'bhanuhastakalaapp/contact.html', {})

#admin
#
# def adminhome(request):
#     return render(request, 'adminpages/adminhome.html')

class adminhome(ListView):
    template_name = 'adminpages/adminhome.html'
    queryset = Product.objects.all()
    context_object_name = 'productlist'

class addProduct(SuccessMessageMixin, CreateView,):
    template_name = 'adminpages/addproduct.html'
    form_class = ProductForm
    success_url = reverse_lazy('BhanuHastakalaApp:addproduct')

    success_message = "New Product Add Successfully"


class ProductEdit(SuccessMessageMixin, UpdateView):
    template_name = 'adminpages/EditProduct.html'
    model = Product
    fields = ('title','slug', 'category', 'image', 'market_price','selling_price','description','warrenty','return_policy')
    success_url = reverse_lazy('BhanuHastakalaApp:adminhome')
    success_message = "Update Product Successfully"


class AdminProductDetails(DetailView):
    template_name ="adminpages/adminproductdetails.html"
    model = Product
    context_object_name = 'product'

class AdminProductDelete(DeleteView):
    template_name = "adminpages/adminproductdelete.html"
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('BhanuHastakalaApp:adminhome')


