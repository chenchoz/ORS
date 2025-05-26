from django.shortcuts import render,redirect
from irsappone import models
from django.utils.timezone import make_aware
from datetime import datetime
from django.db.models import Q
from irsappone.models import Incident
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'irsappone/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('incidents')

class RegisterPage(FormView):
    template_name = 'irsappone/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('incidents')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('incidents')
        return super().get(request, *args, **kwargs)
        

    




class IncidentList(LoginRequiredMixin,ListView):
    model = Incident
    template_name = 'irsappone/incident_list.html'  # This is important!
    context_object_name = 'incidents'  # Match this with your for loop in HTML
    
    def get_queryset(self):
        search_input = (self.request.GET.get('search-area') or '').strip()
        queryset = super().get_queryset()
        
        if search_input:
            try:
                search_date = datetime.strptime(search_input, '%Y-%m-%d').date()
                search_date = make_aware(datetime.combine(search_date, datetime.min.time()))
            except ValueError:
                search_date = None

            # Filter by all fields including date if date parsing successful
            queryset = queryset.filter(
                Q(call_sign__icontains=search_input) |
                Q(controller_name__icontains=search_input) |
                Q(occurrence__icontains=search_input) |
                Q(aircraft_type__icontains=search_input) |
                Q(detail_report__icontains=search_input) |
                (Q(date=search_date) if search_date else Q())
        )

        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['search_input'] = self.request.GET.get('search-area') or ''
    #     return context




class IncidenDetail(LoginRequiredMixin,DetailView):
    model = Incident
    context_object_name = 'incident'  # Match this with your for loop in HTML

class IncidentCreate(LoginRequiredMixin,CreateView):
    model = Incident
    fields = '__all__'  
    success_url = reverse_lazy('incidents')

    def  form_valid(self, form):
        form.instance.user = self.request.user
        return super(IncidentCreate, self).form_valid(form)

class IncidentUpdate(LoginRequiredMixin,UpdateView):
    model = Incident
    fields = '__all__'
    success_url = reverse_lazy('incidents')

class DeleteView(LoginRequiredMixin,DeleteView):
    model = Incident
    context_object_name = 'incident'
    success_url = reverse_lazy('incidents')


