"""webdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from courses import views
from webdev import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n', include('django.conf.urls.i18n')),
    # path("courses/<slug:slug>", views.themes_of_course, name="themes_of_course"),
]

urlpatterns += i18n_patterns(
    path("", views.home, name="home"),
    path("courses", views.courses, name="courses"),
    path("contact", views.contact, name="contact"),
    path("courses/<slug:slug>/", views.themes_of_course, name="themes_of_course"),
    path('courses/<slug:slugCourse>/<slug:slugTheme>', views.theme, name="theme"),
    path('courses/<slug:slugCourse>/<slug:slugTheme>/<slug:slugQuiz>', views.quiz, name="quiz")
)

if settings.DEBUG is False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
