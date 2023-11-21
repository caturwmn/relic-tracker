from django.urls import path
from main.views import show_main, create_relic, show_xml, show_json, show_json_by_id, show_xml_by_id
from main.views import register, login_user, logout_user, edit_Relic, delete_relic
from main.views import get_relic_json, add_relic_ajax, delete_relic_ajax, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-relic', create_relic, name='create_relic'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-relic/<int:id>', edit_Relic, name='edit_relic'),
    path('delete/<int:id>', delete_relic, name='delete_relic'),
    path('delete-ajax/<str:name>', delete_relic_ajax, name='delete_relic_ajax'),
    path('get-relic/', get_relic_json, name='get_relic_json'),
    path('create-relic-ajax/', add_relic_ajax, name='add_relic_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]