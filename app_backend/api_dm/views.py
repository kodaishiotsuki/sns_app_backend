from rest_framework import generics, permissions, authentication  # REST Frameworkの主要モジュールをインポート
from api_dm import serializers  # メッセージのシリアライザーモジュールをインポート
from core.models import Message  # 使用するMessageモデルをインポート
from rest_framework import viewsets  # ViewSetを使うためのモジュール
from rest_framework.response import Response  # APIレスポンスを返すためのモジュール
from rest_framework import status  # HTTPステータスコードを使用するためのモジュール


# メッセージを管理するViewSet
class MessageViewSet(viewsets.ModelViewSet):
    """
    メッセージの作成、表示、更新、削除を管理するAPIビュー。
    このViewSetでは、ログインユーザーが送信したメッセージだけを操作できます。
    """
    queryset = Message.objects.all()  # メッセージの全データをクエリセットに設定
    serializer_class = serializers.MessageSerializer  # MessageSerializerを使用してデータをシリアライズ
    authentication_classes = (authentication.TokenAuthentication,)  # トークン認証を使用
    permission_classes = (permissions.IsAuthenticated,)  # 認証されたユーザーのみアクセス可能

    # ログインユーザーが送信したメッセージだけを取得
    def get_queryset(self):
        """
        ログインユーザーが送信したメッセージのみをフィルタリングして取得。
        """
        return self.queryset.filter(sender=self.request.user)  # 送信者が現在のユーザーであるメッセージのみを取得

    # メッセージを作成する際に、送信者を自動的にログインユーザーに設定
    def perform_create(self, serializer):
        """
        メッセージを作成する際、送信者として自動的にログインユーザーを設定して保存。
        """
        serializer.save(sender=self.request.user)  # ログインユーザーを送信者として設定

    # メッセージの削除を許可しない
    def destroy(self, request, *args, **kwargs):
        """
        メッセージの削除を拒否する。
        """
        response = {'message': 'Delete DM is not allowed'}  # 削除が許可されていないことをメッセージで返す
        return Response(response, status=status.HTTP_400_BAD_REQUEST)  # 400エラー（不正リクエスト）を返す

    # メッセージの更新（PUT）は許可しない
    def update(self, request, *args, **kwargs):
        """
        メッセージの更新（PUT）を拒否する。
        """
        response = {'message': 'Update DM is not allowed'}  # 更新が許可されていないことをメッセージで返す
        return Response(response, status=status.HTTP_400_BAD_REQUEST)  # 400エラーを返す

    # メッセージの部分更新（PATCH）は許可しない
    def partial_update(self, request, *args, **kwargs):
        """
        メッセージの部分更新（PATCH）を拒否する。
        """
        response = {'message': 'Patch DM is not allowed'}  # 部分更新が許可されていないことをメッセージで返す
        return Response(response, status=status.HTTP_400_BAD_REQUEST)  # 400エラーを返す


# 受信したメッセージの一覧を表示するViewSet
class InboxListView(viewsets.ReadOnlyModelViewSet):
    """
    受信したメッセージの一覧を表示するビュー。
    メッセージを読み取るだけのため、更新や削除などはできない。
    """
    queryset = Message.objects.all()  # メッセージの全データをクエリセットに設定
    serializer_class = serializers.MessageSerializer  # MessageSerializerを使用してデータをシリアライズ
    authentication_classes = (authentication.TokenAuthentication,)  # トークン認証を使用
    permission_classes = (permissions.IsAuthenticated,)  # 認証されたユーザーのみアクセス可能

    # ログインユーザーが受信したメッセージだけを取得
    def get_queryset(self):
        """
        ログインユーザーが受信したメッセージのみをフィルタリングして取得。
        """
        return self.queryset.filter(receiver=self.request.user)  # 受信者が現在のユーザーであるメッセージのみを取得
