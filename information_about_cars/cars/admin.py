from django.contrib import admin
from .models import Car, Comment

class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'owner', 'created_at', 'updated_at')  # Отображаемые поля в списке
    search_fields = ('make', 'model', 'owner__username')  # Поля для поиска
    list_filter = ('year', 'owner')  # Фильтры для удобства

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'car', 'created_at')  # Отображаемые поля в списке
    search_fields = ('author__username', 'car__make', 'car__model')  # Поля для поиска
    list_filter = ('author', 'car')  # Фильтры для удобства

# Регистрируем модели в административной панели
admin.site.register(Car, CarAdmin)
admin.site.register(Comment, CommentAdmin)
