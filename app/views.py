from django.shortcuts import render, redirect
from app.models import DogProduct, Purchase, DogTag
from django.views import View
from app.forms import NewDogTagForm
from datetime import datetime
from django.contrib import messages

# Create your views here.
class Home(View):
    def get(self, request):
        products = DogProduct.objects.all()
        return render(request, "home.html", {"dog_products": products})


class DogProductDetail(View):
    def get(self, request, dog_product_id):
        product = DogProduct.objects.get(id=dog_product_id)
        return render(request, "dog_product_detail.html", {"dog_product": product})


class PurchaseDogProduct(View):
    def post(self, request, dog_product_id):
        product = DogProduct.objects.get(id=dog_product_id)
        if product.quantity != 0:
            product.quantity -= 1
            product.save()
            p = Purchase.objects.create(
                dog_product=product, purchased_at=datetime.now()
            )
            messages.success(request, f"Purchased {product.name}")
            return redirect("purchase_detail", p.id)
        else:
            messages.error(request, f"{product.name} is out of stock")
            return redirect("dog_product_detail")


class PurchaseDetail(View):
    def get(self, request, purchase_id):
        detail = Purchase.objects.get(id=purchase_id)
        return render(request, "purchase_detail.html", {"purchase": detail})


class NewDogTag(View):
    def get(self, request):
        form = NewDogTagForm(request.GET)
        return render(request, "new_dog_tag.html")

    def post(self, request):
        form = NewDogTagForm(request.POST)
        if form.is_valid():
            t = DogTag.objects.create(
                owner_name=form.cleaned_data["owner_name"],
                dog_name=form.cleaned_data["dog_name"],
                dog_birthday=form.cleaned_data["dog_birthday"],
            )
            return redirect("dog_tag_list")
        else:
            form = NewTicketForm()
            return render(request, "new_dog_template.html", {"form": form})
            

class DogTagList(View):
    def get(self, request):
        tags = DogTag.objects.all()
        return render(request, "dog_tag_list.html", {"dog_tags": tags})
