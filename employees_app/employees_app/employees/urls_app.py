from django.urls import path

from employees_app.employees.views import department_details, list_departments, create, not_found

urlpatterns = (
    path('create/', create),
    path('<int:department_id>/', department_details, name='department details'),
    path('', list_departments, name='list departments'),
    path('filter/by/order-by/', list_departments, name='custom url'),

    path('not-found/', not_found),
)
