from django.urls import path

from product.views import Index, Detail

urlpatterns = [
    path('', Index.as_view()),
    path('detail', Detail.as_view())
]
