from todo import views
from django.urls import path

urlpatterns=[
    path('add/',views.add),
    path('delete/<int:tid>', views.delete),
    path('update/<int:tid>', views.update)
]
