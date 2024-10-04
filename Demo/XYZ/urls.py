"""
URL configuration for Demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.abc,name='abc'),  # now url for app is localhost:8000/XYZ and for project  is 8000 (abc is by default)
    path('abcd/',views.abcd,name='abcd'),   # localhost:8000/XYZ/abcd
    path('<int:chai_id>/',views.chai_detail,name='chai_detail'),  # if any integer come then call chai_details view
    path('store/',views.chai_store_view,name='chai_store_view'),
]
