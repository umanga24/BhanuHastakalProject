from django.urls import path
from .import views



app_name = 'BhanuHastakalaApp'

urlpatterns = [
    path('', views.index.as_view(), name='index'),

    path('product-details/<slug:slug>/', views.ProductDetails.as_view(), name='product-details'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('all-product/', views.AllProduct.as_view(), name='all-product'),
    path('Bed/', views.Bed.as_view(), name = 'bed'),
    path('Dinning-table/', views.Dinning.as_view(), name = 'Dinning-table'),
    path('Sofa/', views.Sofa.as_view(), name = 'sofa'),
    path('Cup-Board/', views.Cup.as_view(), name = 'cup'),
    path('about/', views.about.as_view(), name='about'),
    path('contact/', views.contact, name='contact'),

    path('adminhome/', views.adminhome.as_view(), name='adminhome'),
    path('add-new/', views.addProduct.as_view(), name='addproduct'),
    path('edit-product/edit/<slug:slug>/', views.ProductEdit.as_view(), name='edit-product'),
    path('product-detail/<slug:slug>/', views.AdminProductDetails.as_view(), name='product-detail'),
    path('product-delete/<slug:slug>/', views.AdminProductDelete.as_view(), name='product-delete'),


]