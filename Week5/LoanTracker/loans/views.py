from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Loan
from .forms import LoanForm



class LoanListView(ListView):
    model = Loan
    template_name = 'loans/loan_list.html'
    context_object_name = 'loans'



class LoanDetailView(DetailView):
    model = Loan
    template_name = 'loans/loan_detail.html'
    context_object_name = 'loan'
    
    
    
class LoanCreateView(CreateView):
    model = Loan
    template_name = 'loans/loan_form.html'
    form_class = LoanForm
    success_url = '/loans/list'



class LoanUpdateView(UpdateView):
    model = Loan
    template_name = 'loans/loan_form.html'
    form_class = LoanForm
    success_url = '/loans/list'

