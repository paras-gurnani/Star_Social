from django.shortcuts import render
from django.urls import reverse_lazy
from accounts import forms
from django.views.generic import (CreateView,TemplateView)
# Create your views here.

class Signup(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
