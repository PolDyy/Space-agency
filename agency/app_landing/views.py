from django.shortcuts import render
from django.views import View

from .models import Image


class MainPageView(View):

    def get(self, request):

        slider_items = Image.objects.all()
        context = {'slider_items': slider_items}

        template_name = 'main.html'

        return render(request, template_name, context=context)


