from django.conf.urls import url
from qa.views import question_answer, new
from qa.views import test, question, question_detail, popular
from qa.views import user_signup, user_login, user_logout

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
    url(r'^popular/', popular, name='popular'),
    url(r'^ask/', question, name='question'),
    url(r'^answer/', question_answer, name='question_answer'),
    url(r'^signup/', user_signup, name='signup'),
    url(r'^login/', user_login, name='login'),
    url(r'^logout/', user_logout, name='logout'),
    url(r'^new/', test, name='new'),
]
