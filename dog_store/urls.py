"""dog_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Home.as_view(), name="home"),
    path(
        "dog-product/<dog_product_id>",
        views.DogProductDetail.as_view(),
        name="dog_product_detail",
    ),
    path(
        "dog-product/<dog_product_id>/purchase",
        views.PurchaseDogProduct.as_view(),
        name="purchase_dog_product",
    ),
    path(
        "purchase/<purchase_id>", views.PurchaseDetail.as_view(), name="purchase_detail"
    ),
    path("dogtag/new", views.NewDogTag.as_view(), name="new_dog_tag"),
    path("dogtag", views.DogTagList.as_view(), name="dog_tag_list"),
    path("cat-product", views.Home2.as_view(), name="home2"),
    path(
        "cat-product/<cat_product_id>",
        views.CatProductDetail.as_view(),
        name="cat_product_detail",
    ),
    path(
        "cat-product/<cat_product_id>/purchase",
        views.PurchaseCatProduct.as_view(),
        name="purchase_cat_product",
    ),
    path(
        "catpurchase/<cat_purchase_id>",
        views.CatPurchaseDetail.as_view(),
        name="purchase_detail_two",
    ),
    path("cattag/new", views.NewCatTag.as_view(), name="new_cat_tag"),
    path("cattag", views.CatTagList.as_view(), name="cat_tag_list"),
]
