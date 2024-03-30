from django.urls import path, include

from .views import Uzbek_poets,shoirlarhoirlar,shoirlarning_rasmlari

urlpatterns = [

    path('',Uzbek_poets, name = "O'zbek shoirlari")
    path('',shoirlar,name = "Shoirlar")
    path('',shoirlarning_rasmlari)
]
