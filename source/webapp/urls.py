from django.urls import path
from webapp.views import index_view, cat_states_view


urlpatterns = [
    path('', index_view),
    path('cat_stats/', cat_states_view)
]


