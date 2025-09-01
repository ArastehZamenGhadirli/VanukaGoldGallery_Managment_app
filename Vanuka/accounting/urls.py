from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="accounting_dashboard"),
    path("invoices/", views.invoice_list, name="invoice_list"),
    path("invoices/<int:invoice_id>/", views.invoice_detail, name="invoice_detail"),
    path("transactions/", views.transaction_list, name="transaction_list"),
    path("transactions/<int:transaction_id>/", views.transaction_detail, name="transaction_detail"),
]


