from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):

    context = {
        'title':  _('Home'),
        'home' : 'active',

    }

    return render(request, 'home/index.html', context)
def about(request):

    context = {
        'title':  _('About'),
        'about' : 'active',

    }

    return render(request, 'home/about.html', context)
def contactUs(request):

    context = {
        'title':  _('Contact Us'),
        'contact' : 'active',

    }

    return render(request, 'home/contact_us.html', context)
def termsAndConditions(request):

    context = {
        'title':  _('Terms and Conditions'),
        'terms' : 'active',

    }

    return render(request, 'home/terms_and_conditions.html', context)
def test(request):

    context = {
        'title':  _('Test'),
        'test' : 'active',

    }

    return render(request, 'home/test.html', context)