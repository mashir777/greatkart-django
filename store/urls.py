from django.urls import path
from . import views 

urlpatterns = [
    path('', views.store, name='store'),

    # ✔ SEARCH URL MUST COME BEFORE CATEGORY
    path('search/', views.search, name='search'),

    # ✔ CATEGORY URL WITHOUT "category/" PREFIX (GreatKart tutorial style)
    path('<slug:category_slug>/', views.store, name='products_by_category'),

    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
