from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from core import models

# カスタムユーザー管理画面の定義
class UserAdmin(BaseUserAdmin):
    # ユーザーのリスト表示時に使用するフィールド
    ordering = ['id']
    list_display = ['email']
    
    # ユーザー詳細画面のフィールドセット
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ()}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    
    # 新規ユーザー作成画面でのフィールドセット
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),
    )

# 登録するモデルを管理画面に追加
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile)
admin.site.register(models.Message)
admin.site.register(models.FriendRequest)
