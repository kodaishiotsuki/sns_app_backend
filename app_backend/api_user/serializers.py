from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from core.models import Profile,FriendRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # ユーザーモデルを取得
        fields = ('id', 'email', 'password')  # シリアライズ対象のフィールドを定義
        extra_kwargs = {'password': {'write_only': True}}  # パスワードは書き込み専用（レスポンスには含まれない）

    def create(self, validated_data):
        # バリデーション済みのデータを使ってユーザーを作成
        user = get_user_model().objects.create_user(**validated_data)
        # トークンを生成してユーザーに紐付ける（APIトークン認証に使用）
        Token.objects.create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    # created_on フィールドは 'YYYY-MM-DD' 形式にフォーマットされ、読み取り専用です
    created_on = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Profile  # 対象のモデルは Profile
        fields = ('id', 'nickName', 'img', 'userPro', 'created_on')  # シリアライズ対象のフィールド
        extra_kwargs = {'userPro': {'read_only': True}}  # userPro フィールドは読み取り専用



class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest  # 対象のモデルは FriendRequest
        fields = ('id', 'askFrom', 'askTo', 'approved')  # シリアライズ対象のフィールド
        extra_kwargs = {'askFrom': {'read_only': True}}  # askFrom フィールドは読み取り専用

