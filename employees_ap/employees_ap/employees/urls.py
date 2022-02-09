from django.urls import path

from employees_ap.employees.views import department_details, list_departments, not_found, create

urlpatterns = (
    path('create/', create),
    path('<department_id>/', department_details, name='department details'),

    path('', list_departments, name='list departments'),
    path('filter/by/order-by/', list_departments, name='custom url'),
    path('not-found/', not_found),
)
