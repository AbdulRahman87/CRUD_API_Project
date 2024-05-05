from api import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.NotesApi, basename="NotesApi")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name="Home"),
    path('notedelete/', views.note_delete, name="DeleteNote"),
    path("notesapi/", include(router.urls)),
    path("notesupdate/", views.update_note, name="UpdateNote"),
]