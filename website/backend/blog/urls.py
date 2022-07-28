from .views import BlogPageView
from rest_framework.routers import DefaultRouter

app_name = "blog"

router = DefaultRouter()
router.register('blog', BlogPageView)
urlpatterns = router.urls