from django.urls import path
from .views import add_parent, get_parent, update_parent, delete_parent, add_child, get_child, update_child, \
    delete_child, add_blog, update_blog, get_blog, delete_blog, home_feed, customize_feed

urlpatterns = [
    path('add_parent/', add_parent, name='add_parent'),
    path('get_parent/<int:parent_id>', get_parent, name='get_parent'),
    path('update_parent/<int:parent_id>', update_parent, name='update_parent'),
    path('delete_parent/<int:parent_id>', delete_parent, name='delete_parent'),

    path('add_child/', add_child, name='add_child'),
    path('get_child/<int:child_id>', get_child, name='get_child'),
    path('update_child/<int:child_id>', update_child, name='update_child'),
    path('delete_child/<int:child_id>', delete_child, name='delete_child'),

    path('add_blog/', add_blog, name='add_blog'),
    path('get_blog/<int:blog_id>/', get_blog, name='get_blog'),
    path('update_blog/<int:blog_id>/', update_blog, name='update_blog'),
    path('delete_blog/<int:blog_id>/', delete_blog, name='delete_blog'),

    path('home_feed/<int:parent_id>/', home_feed, name='home_feed'),
    path('customize_feed/<int:parent_id>/', customize_feed, name='customize_feed'),
]
