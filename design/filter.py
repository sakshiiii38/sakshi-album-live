import django_filters 

from .models import *
from django_filters import DateFilter, CharFilter

class CategoryFilter(django_filters.FilterSet):
    
   
    class Meta:
        model = Category
        fields='__all__'
        