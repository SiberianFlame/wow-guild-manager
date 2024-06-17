from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView

from wgm_app_auth.models import UserProfile


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'wgm_app_auth/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(
            self.request,
            username=username,
            password=password)

        login(request=self.request, user=user)
        return response
