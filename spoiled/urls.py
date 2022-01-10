from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


app_name = "spoiled"
urlpatterns = [
    path("<int:pk_shop>", views.SpoiledListView.as_view(), name="all"),
    # path("add/<int:pk_shop>", views.NomenclatureSearch.as_view(), name="search_nomenclature"),
    path("add/create/<int:pk_shop>", views.SpoiledCreateView.as_view(), name="create_spoiled"),
    path('pic/<int:pk>', views.stream_file, name='pic_picture'),
    path('spoiled/<int:pk>', views.SpoiledDetailView.as_view(), name='spoiled_detail'),
    path('spoiled/<int:pk>/delete',
         views.SpoiledDeleteView.as_view(), name='spoiled_delete'),
    path('spoiled/<int:pk>/update',
         views.SpoiledUpdateView.as_view(), name='spoiled_update'),

]

