from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #rotas para autenticacao
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_obtain_pair"),
    
    #rotas apps
    path("api/v1/", include("apiLista.urls"))
]
