from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Blog Api',
        description='Api chiqarish',
        default_version='v1',
        terms_of_service='',
        contact=openapi.Contact(email='hakimkhon94@gmail.com'),
        license=openapi.License(name='Blog Api litsenziyasi'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('post.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration', include('dj_rest_auth.registration.urls')),
    path('api/v1/allauth', include('allauth.urls')), #*allauth/confirm-mail
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redox/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    # path('openapi', get_schema_view(
    #     title='Blog Api',
    #     description='DRF orqali api vhiqarishni urganyapmiz',
    #     version='1.0.0'
    # ), name='openapi-schema'),
]
