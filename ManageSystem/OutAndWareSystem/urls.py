from django.urls import path, include
import OutAndWareSystem.views

urlpatterns = [
    path('index', OutAndWareSystem.views.index),
    path('prices', OutAndWareSystem.views.get_price),
    path('wx_prices', OutAndWareSystem.views.wx_price),
    path('ware', OutAndWareSystem.views.get_ware),
    path('issue', OutAndWareSystem.views.get_issue),
    path('stocks', OutAndWareSystem.views.get_stocks),

    path('add_price', OutAndWareSystem.views.add_price),
    path('add_ware', OutAndWareSystem.views.add_ware),
    path('add_issue', OutAndWareSystem.views.add_issue),
    path('prices_search', OutAndWareSystem.views.prices_search),
    path('ware_search', OutAndWareSystem.views.ware_search),
    path('issue_search', OutAndWareSystem.views.out_search),
    path('delete/<int:good_id>', OutAndWareSystem.views.delete_price),
    path('jump_update_price/<int:good_id>', OutAndWareSystem.views.jump_update_price),
    path('jump_update_ware/<int:good_id>', OutAndWareSystem.views.jump_update_ware),
    path('delete_ware/<int:ware_id>', OutAndWareSystem.views.delete_ware),

    path('update_price', OutAndWareSystem.views.update_price),
    path('update_ware', OutAndWareSystem.views.update_ware),

    path('calculate', OutAndWareSystem.views.calculate)
]
