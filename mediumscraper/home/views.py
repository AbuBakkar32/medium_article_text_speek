import warnings

import bs4
import requests as req
from django.shortcuts import render

from .forms import NameForm

warnings.simplefilter('ignore')


def get_link(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            res = req.get(form.cleaned_data['urllink'])
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            content = ''
            if soup.find('article'):
                for i in soup.select('article'):
                    content += i.getText()
            else:
                print("This is not a medium article link..!")
                return render(request, 'home/index.html', {'form': form,
                                                           'text': "We could not find an article in this page. Please make sure this is a medium article link."})
            form = NameForm()
            val = content

        else:
            return render(request, 'home/index.html', {'form': form,
                                                       'text': "We could not find an article in this page. Please make sure this is a medium article link."})
    else:
        form = NameForm()
        val = "Please Enter a link"

    return render(request, 'home/index.html', {'form': form, 'text': val})
