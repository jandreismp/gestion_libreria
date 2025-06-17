from django.urls import path
from .views import LibroListView, LibroCreateView, LibroUpdateView, LibroDeleteView, LibroDetailView

urlpatterns = [
    path('libros/', LibroListView.as_view(), name='libro-list'),
    path('libros/nuevo/', LibroCreateView.as_view(), name='libro-create'),
    path('libros/<str:pk>/', LibroDetailView.as_view(), name='libro-detail'),
    path('libros/<str:pk>/editar/', LibroUpdateView.as_view(), name='libro-update'),
    path('libros/<str:pk>/eliminar/', LibroDeleteView.as_view(), name='libro-delete'),
]