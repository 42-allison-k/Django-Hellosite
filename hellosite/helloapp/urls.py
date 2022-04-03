from django.urls import path
from helloapp.views import HelloWorldView, HelloNameView, GoodbyeView

urlpatterns = [
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('<name>', HelloNameView.as_view(), name='hello_name'),
    path('goodbye/<name>', GoodbyeView.as_view(), name='goodbye'),
    ]