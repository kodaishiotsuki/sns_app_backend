from rest_framework import permissions  # REST Frameworkのパーミッションモジュールをインポート

# プロフィールに対するカスタムパーミッションクラス
class ProfilePermission(permissions.BasePermission):
    """
    Profileオブジェクトに対するアクセス権をカスタマイズするクラス。
    """
    def has_object_permission(self, request, view, obj):
        """
        リクエストに基づいて、特定のオブジェクト（Profile）へのアクセス権を決定するメソッド。

        - SAFE_METHODS（GET, HEAD, OPTIONS）は全てのユーザーに許可。
        - 更新や削除などの安全でないメソッドの場合、ログインユーザーがオブジェクトの所有者かどうかを確認。
        """
        # 安全なメソッド（GET, HEAD, OPTIONS）は常に許可
        if request.method in permissions.SAFE_METHODS:
            return True

        # それ以外のメソッド（PUT, DELETEなど）は、オブジェクトの所有者（userPro）が現在のログインユーザーかどうか確認
        return obj.userPro.id == request.user.id
