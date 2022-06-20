from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqat ko'rish uchun ruhsat berildi
        if request.method in permissions.SAFE_METHODS:
            return True
        # faqat avtorga uzgartirish uchun ruhsat berildi
        return obj.author == request.user
