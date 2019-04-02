from django.conf.urls import url
# from addData import add_student, add_grade
import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^interface_case/$', views.interface_case, name='interface_case'),
    url(r'^module/$', views.modules, name='modules'),
    url(r'^drivers/$', views.driver, name='driver'),
    url(r'^ui-element/$', views.ui_element, name='ui-element'),
    url(r'^user/$', views.user_manage, name='user'),
    url(r'^project_ajax$', views.project_ajax, name='project_ajax'),
    url(r'^test$', views.test, name='test'),

]
