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

    path('post/new/', addPost, name="addPost"),
    path('serie/new/', addSerie, name="addSerie"),
    path('tag/new/', addTag, name="addTag"),

    path('post/delete/<int:pk>', deletePost, name="deletePost"),
    path('serie/delete/<int:pk>', deleteSerie, name="deleteSerie"),
    path('tag/delete/<int:pk>', deleteTag, name="deleteTag"),

    path('post/<slug:slug>', detailPost, name="detailPost"),
    path('tag/<str:subject>', detailTag, name="detailTag"),

    path('post/edit/<int:pk>', editPost, name="editPost"),
    path('tag/edit/<str:subject>', editTag, name="editTag"),
]
