"""YaMDb URL Configuration
"""
from django.contrib import admin

from django.urls import include, path

from django.views.generic import TemplateView


from users.views import UserCreateViewSet, UserReceiveJWTViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet, basename='user')
urlpatterns = router_v1.urls


urlpatterns = [
    path('api/v1/auth/signup/',
         UserCreateViewSet.as_view({'post': 'create'}),
         name='signup'),
    path(
        'api/v1/auth/token/',
        UserReceiveJWTViewSet.as_view({'post': 'create'}),
        name='token'),
    path('api/v1/', include(router_v1.urls)),
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'),
]
