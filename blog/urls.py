from django.urls import path, include

from .views import (
    index, series, about, tags, 
    addPost, addSerie, addTag,
    deletePost, deleteSerie, deleteTag,
    editPost, editTag,
    detailPost, detailTag,
)

urlpatterns = [
    path('', index, name='index'),
    path('series/', series, name='series'),
    path('about/', about, name='about'),
    path('tags/', tags, name='tags'),

    path('newPost/', addPost, name="addPost"),
    path('newSerie/', addSerie, name="addSerie"),
    path('newTag/', addTag, name="addTag"),

    path('deletePost/<int:pk>', deletePost, name="deletePost"),
    path('deleteSerie/<int:pk>', deleteSerie, name="deleteSerie"),
    path('deleteTag/<int:pk>', deleteTag, name="deleteTag"),

    path('detail/<slug:slug>', detailPost, name="detailPost"),
    path('detailTag/<str:subject>', detailTag, name="detailTag"),

    path('editPost/<int:pk>', editPost, name="editPost"),
    path('editTag/<str:subject>', editTag, name="editTag"),
]
