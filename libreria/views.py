from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Libro, Autor, Editor

class LibroListView(ListView):
    model = Libro
    template_name = 'libro_list.html'
    context_object_name = 'libros'

class LibroCreateView(CreateView):
    paginate_by = 150
    model = Libro
    fields = ['isbn', 'tema', 'precio', 'id_autor', 'id_editor', 'stock']
    template_name = 'libro_form.html'
    success_url = reverse_lazy('libro-list')

    def get_queryset(self):
        queryset = super().get_queryset()
        tema = self.request.GET.get('tema')
        if tema:
            queryset = queryset.filter(tema__icontains=tema)
        return queryset.order_by('isbn')

class LibroUpdateView(UpdateView):
    model = Libro
    fields = ['isbn', 'tema', 'precio', 'id_autor', 'id_editor', 'stock']
    template_name = 'libro_form.html'
    success_url = reverse_lazy('libro-list')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'libro_confirm_delete.html'
    success_url = reverse_lazy('libro-list')

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro_detail.html'