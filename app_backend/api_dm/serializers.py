from rest_framework import serializers
from core.models import Message, User, Profile, FriendRequest
from django.db.models import Q

# 友達リストをフィルタリングするためのカスタムフィールド
class FriendsFilter(serializers.PrimaryKeyRelatedField):
    # クエリセットを取得するメソッド
    def get_queryset(self):
        # リクエストしたユーザーを取得
        request = self.context['request']
        # リクエストしたユーザー宛ての友達リクエストの中で、承認されたものだけをフィルタリング
        friends = FriendRequest.objects.filter(Q(askTo=request.user) & Q(approved=True))

        # 友達のIDをリストに追加
        list_friend = []
        for friend in friends:
            list_friend.append(friend.askFrom.id)
        
        # 友達リストに含まれるユーザーだけをクエリセットとして返す
        queryset = User.objects.filter(id__in=list_friend)
        return queryset

# メッセージのシリアライザー
class MessageSerializer(serializers.ModelSerializer):
    # 受信者フィールドに FriendsFilter を適用し、友達の中からのみ受信者を選択可能にする
    receiver = FriendsFilter()

    class Meta:
        model = Message  # 対象モデルは Message
        fields = ('id', 'message', 'sender', 'receiver')  # シリアライズするフィールドを指定
        extra_kwargs = {'sender': {'read_only': True}}  # 送信者フィールドは読み取り専用

    # 送信者は自動的にログインユーザーとして設定され、受信者は友達リストから選択可能です。
