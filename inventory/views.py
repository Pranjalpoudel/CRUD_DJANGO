from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Item, Category
from .forms import ItemForm, CategoryForm

class ItemListView(ListView):
    model = Item
    template_name = 'inventory/item_list.html'
    context_object_name = 'items'
    ordering = ['-updated_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        status = self.request.GET.get('status')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | 
                Q(serial_number__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        if category:
            queryset = queryset.filter(category__id=category)
        if status:
            queryset = queryset.filter(status=status)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['status_choices'] = Item.STATUS_CHOICES
        return context

class ItemDetailView(DetailView):
    model = Item
    template_name = 'inventory/item_detail.html'
    context_object_name = 'item'

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('item_list')

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('item_list')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'inventory/item_confirm_delete.html'
    success_url = reverse_lazy('item_list')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'inventory/category_form.html'
    success_url = reverse_lazy('item_list')

