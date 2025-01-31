
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Import your views here
from tasks import views

def home(request):
    return HttpResponse("Welcome to the Task Manager!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Assuming you have the 'tasks' app's URLs set up
    path('', home, name='home'),  # Add this line for the root URL path
]
