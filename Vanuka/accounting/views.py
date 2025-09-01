from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("Welcome to the Accounting Dashboard!")

def invoice_list(request):
    return HttpResponse("List of Invoices")

def invoice_detail(request, invoice_id):
    return HttpResponse(f"Invoice Detail for ID {invoice_id}")

def transaction_list(request):
    return HttpResponse("List of Transactions")

def transaction_detail(request, transaction_id):
    return HttpResponse(f"Transaction Detail for ID {transaction_id}")