from django.conf.urls import include, url
import core.views as coreviews

urlpatterns = patterns('',
    url(r'^$', coreviews.LandingView.as_view()),
)
