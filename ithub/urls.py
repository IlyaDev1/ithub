from django.contrib import admin
from django.urls import path, include
import oge.urls as oge_urls
import mainapp.urls as main_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_app_urls)),
    path('oge/', include(oge_urls))
]
