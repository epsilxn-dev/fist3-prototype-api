from django.contrib import admin
from .models import Commentary, ChildCommentary


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "create_by", "create_dt", "update_dt")


@admin.register(ChildCommentary)
class ChildCommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "parent_comment", "create_by", "create_dt", "update_dt")
