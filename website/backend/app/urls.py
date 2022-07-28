from garpixcms.urls import *  # noqa

urlpatterns = [path('api/', include('review.urls')),
               path('api/', include('blog.urls'))] + urlpatterns  # noqa
