from django.conf.urls import include, url, patterns 
from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('qa.views',                                              
#   url(r'^$', 'test'),                                                              
#   url(r'^login/.*$', 'test', name='login'),                                    
#   url(r'^signup/.*', 'test', name='signup'),                                   
#   url(r'^question/(?P<id>[0-9]+)/$', 'test', name='question'),                 
#   url(r'^ask/.*', 'test', name='ask'),                                         
#   url(r'^popular/.*', 'test', name='popular'),                                 
#   url(r'^new/.*', 'test', name='new'),                                         
#)  

#urlpatterns = [
#    url(r'^', include("qa.urls")),
#    url(r'^admin/', admin.site.urls),
#]

urlpatterns = [  
    url(r'^$', 'qa.views.allq'),
    url(r'^login/.*$', 'qa.views.test'),
    url(r'^signup/.*$', 'qa.views.test'),
    url(r'^question/(?P<q_id>\d+)/$', 'qa.views.show_question'),
    url(r'^ask/.$', 'qa.views.question_add'),
    url(r'^popular/.*$', 'qa.views.popular'),
    url(r'^new/.*$', 'qa.views.post_answer'),
]
