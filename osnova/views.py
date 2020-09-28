from django.views.generic import DetailView, ListView

from .models import *

class BaseView(ListView):
    template_name = 'base.html'
    model = Article
    context_object_name = 'articles'
