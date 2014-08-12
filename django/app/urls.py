from django.conf.urls import patterns, url
from app import views

IDREGEX = r'(?P<id>\d+)'

urlpatterns = patterns(
    '',
#    ex: /api/
    url(r'^$', views.index, name='index'),
#    app/synthesis
    url(r'^synthesis/'+IDREGEX+r'/$', views.synthesis, name='synthesis'),
#    app/singleStep/1
    url(r'^singleStep/'+IDREGEX+r'/$', views.single_step, name='single_step'),
#    app/singleStepHard/2
    url(r'^singleStepHard/'+IDREGEX+r'/$', views.single_step_hard, name='single_step'),
#    app/predictProducts
    url(r'^predictProducts/'+IDREGEX+r'/$', views.predict_products, name='predict_products'),
)