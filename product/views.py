from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Index(TemplateView):
    template_name = 'templates/index.html'


class Detail(TemplateView):
    template_name = 'templates/shop-details.html'
