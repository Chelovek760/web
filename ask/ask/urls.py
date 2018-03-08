"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from qa.views import new,popular,question


urlpatterns = [

    url(r'^$', new),

   # url(r'^init25/', init25),
   # url(r'^login/', login_view),
   # url(r'^signup/', signup),
    #url(r'^ask/', ask),
    # url(r'^answer/', answer),
    url(r'^popular/', popular),
   # url(r'^new/', found),

    #url(r'^admin/', admin.site.urls),
    url(r'^question/^(?P<num>\d+)/$', question),

    #url(r'^', not_found),
]