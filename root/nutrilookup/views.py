from django.shortcuts import render
from . import Webscaper

key = 'DUVrhfkiQygwj18fesQvdwpgbPbrAjP1QDfD9lgt'


# Create your views here.
def main_page(request):
    return render(request=request, template_name="base.html", context=None)


def new_search(request):
    search = request.POST.get('search')
    context = Webscaper.search_item(search)
    print(context)
    return render(request=request, template_name="nutrilookup/new_search.html", context=context)
