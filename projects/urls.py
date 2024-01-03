from django.urls import path
from . import views

urlpatterns = [
path('home', views.home, name = 'home'),
path('projects', views.projectList, name = 'projects'),
path('projects/<int:pk>', views.projectDetail, name ='project-detail'), 
path('tasks', views.taskList, name ='tasks'),
path('tasks/<int:pk>', views.taskDetail, name ='task-detail'),
path('create-task', views.taskCreate, name ='create-task'),
path('create-project', views.ProjectCreateView.as_view(), name ='create-project'), # Here, it's the 'ProjectCreateView' class-based view, with 'as_view()' method called.
path('update-task/<int:pk>', views.TaskUpdateView.as_view(), name ='update-task'),
path('update-project/<int:pk>', views.ProjectUpdateView.as_view(), name ='update-project'),
path('delete-task/<int:pk>', views.TaskDeleteView.as_view(), name ='delete-task'), 
path('delete-project/<int:pk>', views.ProjectDeleteView.as_view(), name ='delete-project'),
path('join-task/<int:pk>', views.joinTask, name ='join-task'),

]

# Django class-based views are views that inherit from a base class provided by Django. They are used to write concise and reusable views
# https://learndjango.com/tutorials/django-best-practices-function-based-views-vs-class
# In summary, class-based views in Django provide a more structured, reusable, and extendable way to create views, 
# especially beneficial in larger or more complex Django applications. They help keep your code DRY (Don't Repeat Yourself) and make it easier to manage and extend.
