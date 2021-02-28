from django.shortcuts import render
from drop.models import book
from django.views.generic import CreateView

class bookcreateview(CreateView):
    model=book
    template_name='book_form.html'
    fields='__all__'
