from django.urls import path
from . import views

app_name="polls"

urlpatterns=[

    # path('quiz/',views.quiz,name='quiz'),
    path('poll/list/', views.polls_list, name='list'),
    path('<int:poll_id>/detail/', views.poll_detail , name='detail'),
    path('list/user/', views.list_by_user, name='list_by_user'),
    path('<int:poll_id>/vote/', views.poll_vote, name='vote'),
    path('resultsdata/<int:poll_id>/',views.resultsData,name='resultsdata'),
    path('add/', views.polls_add, name='add'),

    path('edit/<int:poll_id>/', views.polls_edit, name='edit'),
    path('delete/<int:poll_id>/', views.polls_delete, name='delete_poll'),
    path('end/<int:poll_id>/', views.endpoll, name='end_poll'),
    path('edit/<int:poll_id>/choice/add/', views.add_choice, name='add_choice'),
    path('edit/choice/<int:choice_id>/', views.choice_edit, name='choice_edit'),
    path('delete/choice/<int:choice_id>/',
         views.choice_delete, name='choice_delete'),
    path('pollresult/<int:poll_id>/', views.poll_result, name='pollresult'),

]