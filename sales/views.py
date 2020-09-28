from django.views.generic import ListView
from.models import ProductName
from.models import ProductDetail

class HomeView(ListView):
    model = ProductDetail
    context_object_name = ''
    template_name='home.html'
    template_name='index.html'

    def get_queryset(self):
         queryset = super().get_queryset()
         return queryset.select_related('pr_desc')

    

