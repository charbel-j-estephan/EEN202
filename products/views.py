from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product
from django.http import HttpResponse, Http404
from django.conf import settings
import os


def products_list(request):
    # Filter posts by the 'active' status and publish date <= current time
    products = Product.objects.filter(
        is_active=True, published_date__lte=timezone.now()
    ).order_by("published_date")
    return render(request, "products/products_list.html", {"products": products})


def products_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/post_detail.html", {"product": product})


def download_brochure(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.Brochure:
        file_path = os.path.join(settings.MEDIA_ROOT, str(product.Brochure))
        if os.path.exists(file_path):
            with open(file_path, "rb") as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type="application/pdf")
                response["Content-Disposition"] = (
                    f'attachment; filename="{os.path.basename(file_path)}"'
                )
                return response
    raise Http404("File not found")
