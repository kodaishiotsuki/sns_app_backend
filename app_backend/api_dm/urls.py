from django.urls import path, include  
from rest_framework.routers import DefaultRouter 
from api_dm import views 

# アプリケーションの名前空間を定義。これにより、他のアプリケーションとのURL名の衝突を避ける
app_name = 'dm'

# DefaultRouterのインスタンスを作成
# DefaultRouterは、ViewSetに基づいて自動的にURLを生成します
router = DefaultRouter()

# 'message'というパスに対して、MessageViewSetを登録
# これにより、メッセージ送受信に関連するCRUD（作成、取得、更新、削除）操作が可能になります
# basename='message' は、URL生成時に使われる名前のベースです
router.register('message', views.MessageViewSet, basename='message')

# 'inbox'というパスに対して、InboxListViewを登録
# これにより、受信ボックスに関連する操作（メッセージの表示）を管理できます
router.register('inbox', views.InboxListView, basename='inbox')

# urlpatternsに定義されたパスとViewを対応させる
urlpatterns = [
    # ルーターによって自動生成されたURLパターンをインクルードします
    # 'message/' と 'inbox/' に関連するURLが自動的に生成され、それぞれのViewSetが対応するリクエストを処理します
    path('', include(router.urls)),
]
