from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView

from content.forms import BookForm
from content.models import MainPages, Personal, Galery, Category


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main'] = MainPages.objects.all()[0]
        context['personal'] = Personal.objects.filter(is_active=True).order_by('order')[:4]
        context['galery'] = Galery.objects.filter(is_active=True).order_by('order')
        context['category'] = Category.objects.filter(is_active=True).order_by('order')
        return context


class BookView(FormView):
    form_class = BookForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse_lazy('success'))


class SuccessView(TemplateView):
    template_name = 'success.html'


class CategoryView(DetailView):
    template_name = 'catalog.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main'] = MainPages.objects.all()[0]
        context['personal'] = Personal.objects.filter(is_active=True).order_by('order')[:4]
        context['galery'] = Galery.objects.filter(is_active=True).order_by('order')
        context['category'] = Category.objects.filter(is_active=True).order_by('order')
        return context
