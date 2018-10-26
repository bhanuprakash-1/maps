from django.urls import path

from disater import views

urlpatterns = [
    path('' , views.base , name='base'),
    #disater/person_status
    path('person_status/', views.person_status , name='person_status'),

    #disater/person_status
    path('person_status/<int:person_id>', views.details , name='details'),

    #disater/person_status/value=q
    path('search/',views.search, name='search'),
    #disater/affected_areas
    path('affected_areas/', views.affected_areas, name='affected_areas'),
    #disater/affected_areas/search
    path('/affected_area_search', views.Search_affected_areas, name='Search_affected_areas')

]
