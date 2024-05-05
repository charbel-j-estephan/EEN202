from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.products_list, name="product_list"),
    path("Product/<int:id>/", views.products_detail, name="products_detail"),
    path(
        "download-brochure/<int:product_id>/",
        views.download_brochure,
        name="download_brochure",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
