from django.urls import path
from .import views

urlpatterns=[
    path('',views.list_posts,name='list_posts'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new/',views.new_post,name='new_post'),
    path('post/<int:pk>/edit',views.edit_post,name='edit_post'),
    path('drafts/',views.post_draft_list,name='post_draft_list'),
    path('post/<pk>/publish/',views.post_publish,name='post_publish'),
    path('post/<pk>/delete/',views.delete_post,name='delete_post'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
]
