import json

import requests
from django.conf import settings

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView

from content.forms import BookForm
from content.models import MainPages, Personal, Galery, Category, Product


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
        data = {
            'chat_id': settings.TELEGRAM_GROUP_ID,
            'text': '#phone: {}, #name: {}, #comment: {}'.format(obj.phone, obj.name, obj.comment)}
        data = json.dumps(data)
        requests.post(data=data, headers={
            'Content-Type': 'application/json'},
            url='https://api.telegram.org/bot{}/sendMessage'.format(settings.TELEGRAM_TOKEN)
        )
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
        context['product'] = Product.objects.filter(is_active=True, category=self.object).order_by('order')
        return context
