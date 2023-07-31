from django.urls import path

from apps.product.views import Index

urlpatterns = [
    path('', Index.as_view())
]
