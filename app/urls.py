
from django.urls import path
from app.views import StudentPaginationApi
urlpatterns = [
    path('pagination/',StudentPaginationApi.as_view())

]
