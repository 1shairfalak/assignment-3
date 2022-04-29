from django.urls import path
from . import views
urlpatterns = [
    # path('api/v1/school_create/',views.CreateMedicine, name='school_create'),
    path('api/v1/ShowAllquestion/',views.ShowAll, name='ShowAllquestion'),
    path('api/v1/questionwithdepatmentname/',views.questionwithdepatmentname, name='questionwithdepatmentname'),
    path('api/v1/questionhierarchy/',views.questionhierarchy, name='questionhierarchy'),
     path('api/v1/track_question_subject/',views.tracking, name='questionfilter'),
     path('api/v1/questionaggregation/',views.questionaggregation, name='questionaggregation'),
    # path('api/v1/product_update/<int:pk>/',views.Updateproduct, name='product-update'),
    # path('api/v1/product_delete/<int:pk>/',views.delleteproduct, name='product-delete'),
    # path('api/v1/product_list/',views.ShowAll, name='product_list'),
    # # path('api/v1/product_detail/<int:pk>/',views.Viewproduct, name='product_list'),
    # path('api/v1/get_medicine/',views.GetMedicine, name='get_medicine'),
]