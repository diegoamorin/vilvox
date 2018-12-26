from django.urls import path

from .views import (
    index, series, about, tags, 
    addPost, addSerie, addTag,
    deletePost, deleteSerie, deleteTag,
    editPost, editSerie, editTag,
    detailPost, detailSerie,
    confirmDeletePost, cancelDeletePost,
    confirmDeleteSerie, cancelDeleteSerie,
)

urlpatterns = [
    path('', index, name='index'),
    path('series/', series, name='series'),
    path('about/', about, name='about'),
    path('tags/', tags, name='tags'),

    path('post/new/', addPost, name="addPost"),
    path('serie/new/', addSerie, name="addSerie"),
    path('tag/new/', addTag, name="addTag"),

    path('post/delete/<int:pk>/', deletePost, name="deletePost"),
    path('post/delete/confirm/<int:pk>', confirmDeletePost, name="confirmDeletePost"),
    path('post/delete/cancel/<slug:slug>', cancelDeletePost, name="cancelDeletePost"),

    path('serie/delete/<int:pk>/', deleteSerie, name="deleteSerie"),
    path('serie/delete/confirm/<int:pk>', confirmDeleteSerie, name="confirmDeleteSerie"),
    path('serie/delete/cancel/<slug:slug>', cancelDeleteSerie, name="cancelDeleteSerie"),

    path('tag/delete/<int:pk>/', deleteTag, name="deleteTag"),

    path('post/<slug:slug>/', detailPost, name="detailPost"),
    path('serie/<slug:slug>/', detailSerie, name="detailSerie"),

    path('post/edit/<int:pk>/', editPost, name="editPost"),
    path('serie/edit/<int:pk>/', editSerie, name="editSerie"),
    path('tag/edit/<str:subject>/', editTag, name="editTag"),
]
