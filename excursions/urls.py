from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ExcursionsView.as_view(), name='excursions'),
    path('<int:id>/', views.ExcursionItemView.as_view(), name='excursion_item'),
    re_path(r'^(<excursions>\w+)/(?P<count_human>\w+)', views.ExcursionItemView.as_view(), name='excursion_item'),
    path(r'<int:id>/<int:price>', views.ExcursionCustomItem.as_view(), name='excursion_custom_item'),
    path('check_phone/', views.checkPhone, name='check_phone'),
    path('check_code/', views.checkCode, name='check_code'),

    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),

    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('gallery/<int:id>', views.PointGalleryView.as_view(), name='point')
]
