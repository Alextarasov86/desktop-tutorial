from django.urls import path
from .views import ReviewPageView
from rest_framework.routers import DefaultRouter

app_name = "review"

router = DefaultRouter()
router.register('review', ReviewPageView)
urlpatterns = router.urls
