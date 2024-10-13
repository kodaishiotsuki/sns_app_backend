from django.urls import path, include  # URLパターンを定義するためのモジュールをインポート
from rest_framework.routers import DefaultRouter  # ViewSetのURL自動生成を行うためのDefaultRouterをインポート
from api_user import views  # 使用するビューをインポート

# アプリケーションの名前空間を定義。これにより他のアプリケーションとのURL名の衝突を避ける
app_name = 'user'

# DefaultRouterのインスタンスを作成
# DefaultRouterは、ViewSetに基づいて自動的にURLを生成します
router = DefaultRouter()

# 'profile'というパスに対して、ProfileViewSetを登録
# これにより、プロファイル情報に関するCRUD（作成、取得、更新、削除）操作が可能になります
router.register('profile', views.ProfileViewSet)

# 'approval'というパスに対して、FriendRequestViewSetを登録
# これにより、友達リクエストに関するCRUD操作が可能になります
router.register('approval', views.FriendRequestViewSet)

# urlpatternsに定義されたパスとViewを対応させる
urlpatterns = [
    # 'create/' というURLにアクセスすると、新規ユーザー作成用のCreateUserViewが呼び出される
    path('create/', views.CreateUserView.as_view(), name='create'),

    # 'myprofile/' というURLにアクセスすると、ログイン中のユーザーのプロフィール情報を取得するMyProfileListViewが呼び出される
    path('myprofile/', views.MyProfileListView.as_view(), name='myprofile'),

    # それ以外のURLは、DefaultRouterが自動的に生成したURLを含めて処理する
    # 'profile/' や 'approval/' のパスが自動的に生成され、登録したViewSetがそれぞれ対応します
    path('', include(router.urls)),
]
