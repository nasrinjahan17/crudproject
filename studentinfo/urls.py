
from django.contrib import admin
from django.urls import path
from infoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.student_data,name="add_student"),
    path('student_info/',views.student_info,name="student_info"),
    path('delete/<int:id>/',views.delete_info,name="delete"),
    path('<int:id>/',views.edit_data,name="editdata"),
]
