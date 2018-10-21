
from __future__ import absolute_import
from .models import Follow, Friend, FriendshipRequest, Block


from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]

admin.site.register(UserProfile)
admin.site.register(User, UserProfileAdmin)



class BlockAdmin(admin.ModelAdmin):
    model = Block
    raw_id_fields = ('blocker', 'blocked')


class FollowAdmin(admin.ModelAdmin):
    model = Follow
    raw_id_fields = ('follower', 'followee')


class FriendAdmin(admin.ModelAdmin):
    model = Friend
    raw_id_fields = ('to_user', 'from_user')


class FriendshipRequestAdmin(admin.ModelAdmin):
    model = FriendshipRequest
    raw_id_fields = ('from_user', 'to_user')


admin.site.register(Block, BlockAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(FriendshipRequest, FriendshipRequestAdmin)
