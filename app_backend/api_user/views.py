from django.shortcuts import render
from rest_framework import generics, permissions, authentication  # 汎用APIビュー、パーミッション、認証をインポート
from api_user import serializers  # シリアライザーモジュールをインポート
from core.models import User, Profile, FriendRequest  # 使用するモデルをインポート
from django.db.models import Q  # 複数の条件をフィルタリングするためのQオブジェクトをインポート
from rest_framework import viewsets  # ViewSetを使うためのモジュール
from rest_framework.response import Response  # APIレスポンスを返すためのモジュール
from rest_framework import status  # HTTPステータスコードを使用するためのモジュール
from rest_framework.exceptions import ValidationError  # バリデーションエラーを発生させるためのモジュール
from core import custompermissions  # カスタムパーミッションをインポート

# ユーザー登録用のビュー
class CreateUserView(generics.CreateAPIView):
    """
    新しいユーザーを作成するAPIビュー
    """
    serializer_class = serializers.UserSerializer  # UserSerializerを使用してユーザーを作成

# 友達リクエストの管理を行うViewSet
class FriendRequestViewSet(viewsets.ModelViewSet):
    """
    友達リクエストの作成、表示、更新、削除を管理するAPIビュー
    """
    queryset = FriendRequest.objects.all()  # 友達リクエストの全データを対象に
    serializer_class = serializers.FriendRequestSerializer  # FriendRequestSerializerを使用
    authentication_classes = (authentication.TokenAuthentication,)  # トークン認証を使用
    permission_classes = (permissions.IsAuthenticated,)  # 認証されたユーザーのみアクセス可能

    # 現在のユーザーに関連する友達リクエストのみを表示
    def get_queryset(self):
        """
        ユーザーが送ったか受け取った友達リクエストだけを表示する。
        """
        return self.queryset.filter(Q(askFrom=self.request.user) | Q(askTo=self.request.user))  # ログインユーザーに関連するリクエストのみフィルタリング

    # 友達リクエストを作成する際にログインユーザーを自動的に「askFrom」として設定
    def perform_create(self, serializer):
        """
        友達リクエストを作成する際、リクエストしたユーザーを自動的にaskFromに設定する。
        """
        try:
            # ログイン中のユーザーが送信者として設定され、友達リクエストを保存
            serializer.save(askFrom=self.request.user)
        except:
            # リクエストが重複している場合はバリデーションエラーを発生させる
            raise ValidationError("User can have only unique request")

    # 友達リクエストの削除は許可しない
    def destroy(self, request, *args, **kwargs):
        """
        友達リクエストの削除を拒否する。
        """
        response = {'message': 'Delete is not allowed'}  # 削除は許可されていない旨のメッセージを返す
        return Response(response, status=status.HTTP_400_BAD_REQUEST)  # 400エラー（不正リクエスト）を返す

    # 友達リクエストの部分更新（PATCH）は許可しない
    def update(self, request, *args, **kwargs):
        """
        友達リクエストの更新を拒否する。
        """
        response = {'message': 'Patch is not allowed'}  # 更新は許可されていない旨のメッセージを返す
        return Response(response, status=status.HTTP_400_BAD_REQUEST)  # 400エラー（不正リクエスト）を返す

# プロフィールを管理するViewSet
class ProfileViewSet(viewsets.ModelViewSet):
    """
    ユーザーのプロフィールを表示、作成、更新、削除するためのAPIビュー
    """
    queryset = Profile.objects.all()  # プロフィールの全データを対象に
    serializer_class = serializers.ProfileSerializer  # ProfileSerializerを使用
    authentication_classes = (authentication.TokenAuthentication,)  # トークン認証を使用
    permission_classes = (permissions.IsAuthenticated, custompermissions.ProfilePermission)  # 認証済みユーザーとカスタムパーミッションを適用

    # プロフィールを作成する際、ログイン中のユーザーを自動的に「userPro」として設定
    def perform_create(self, serializer):
        """
        プロフィールを作成する際に、ログイン中のユーザーを自動的にuserProフィールドに設定する。
        """
        serializer.save(userPro=self.request.user)  # ログイン中のユーザー情報を保存

# ログイン中のユーザー自身のプロフィールリストを表示するビュー
class MyProfileListView(generics.ListAPIView):
    """
    ログイン中のユーザーのプロフィールを表示するためのAPIビュー
    """
    queryset = Profile.objects.all()  # プロフィールの全データを対象に
    serializer_class = serializers.ProfileSerializer  # ProfileSerializerを使用
    authentication_classes = (authentication.TokenAuthentication,)  # トークン認証を使用
    permission_classes = (permissions.IsAuthenticated,)  # 認証されたユーザーのみアクセス可能

    # ログイン中のユーザーのプロフィールだけをフィルタリング
    def get_queryset(self):
        """
        ログイン中のユーザーのプロフィールだけをフィルタリングして表示する。
        """
        return self.queryset.filter(userPro=self.request.user)  # ログインユーザーに関連するプロフィールのみフィルタリング
