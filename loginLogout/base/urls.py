from django.contrib import admin
from django.urls import path, include
from.views import profile 
from .views import profile, logoutaccount
from .views import landing_page
from django.urls import path
from . import views
from .views import ChurchEditView
from .views import FeedbackListView




urlpatterns = [
    path('', landing_page, name='landing_page'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', profile, name='profile'),
    path("accounts/logoutaccount/",logoutaccount, name="logout"),
    path('content/', views.content_view, name='content'),
    path('accounts/churches/', views.churches, name='churches'),
    path('accounts/devotional/', views.devotional, name='devotional'),
    path('accounts/church/', views.church, name='church'),
    path('accounts/devotionconts/', views.devotionconts, name='devotionconts'),
    path('accounts/stories/', views.stories, name='stories'),
    path('accounts/news1/', views.news1, name='news1'),
    path('accounts/news2/', views.news2, name='news2'),
    path('accounts/news3/', views.news3, name='news3'),  
    path('accounts/church_form/', views.church_form, name='church_form'),  # This line declares the path for adding a church
    path('accounts/church_edit/<int:pk>/', ChurchEditView.as_view(), name='church_edit'),
    path('accounts/church_confirm_delete/<int:pk>/', views.church_confirm_delete, name='church_confirm_delete'),
  # This line declares the path for adding a church
    path('accounts/content/', views.content, name='content'), 
    path('accounts/feedback/', views.feedback, name='feedback'), 
    path('accounts/thank_you/', views.thank_you, name='thank_you'),
    path('accounts/feedback_list/', views.FeedbackListView.as_view(), name='feedback_list'),
    path('accounts/feedback_detail/<int:pk>/', views.FeedbackDetailView.as_view(), name='feedback_detail'),
    path('accounts/feedback_confirm_delete/<int:pk>/', views.FeedbackDeleteView.as_view(), name='feedback_confirm_delete'),

]




  

 




