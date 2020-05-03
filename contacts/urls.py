from django.urls import path

from contacts.views import PersonList, PersonCreate, PersonUpdate, PersonDetail

app_name = 'contacts'
urlpatterns = [
    path('', PersonList.as_view(), name='person_list'),
    path('new', PersonCreate.as_view(), name='person_create'),
    path('edit/<pk>', PersonUpdate.as_view(), name='person_update'),
    path('detail/<pk>', PersonDetail.as_view(), name='person_detail'),
]
