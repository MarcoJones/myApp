from django.conf.urls import url
# from addData import add_student, add_grade
import views


urlpatterns = [
    url(r'^$', views.index),
]
