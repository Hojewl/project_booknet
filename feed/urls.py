from django.urls import path
from .views import *

app_name = "feed"

urlpatterns = [
    path('', FeedList.as_view(), name='feedList'),
    path('<int:_isbn>', list_feed, name='list_feed'),
    path('myfeed', my_feed, name='myfeed'),
    path('<int:_isbn>/create', create_feed, name='create'),
    path('<int:_isbn>/delete/<int:pk>', FeedDelete.as_view(), name='delete'),
    path('delete/<int:pk>', FeedDelete.as_view(), name='delete_from_myfeed'),
    path('<int:_isbn>/update/<int:pk>', FeedUpdate.as_view(), name='update'),
    path('update/<int:pk>', FeedUpdate.as_view(), name='update_from_myfeed'),
    path('<int:_isbn>/detail/<int:pk>', FeedDetail.as_view(), name='detail'),
    path('like/<int:pk>', LikeView.as_view(), name='like'),
]