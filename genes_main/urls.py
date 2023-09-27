from django.urls import path
from .views import GeneSymbolQuery

urlpatterns = [
    path('genequery/', GeneSymbolQuery.as_view()),
]
