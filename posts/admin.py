"""Posts Admin classes"""

#Django
from django.contrib import admin

#Models
from posts.models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """Posts admin"""

    list_display = ('pk', 'user', 'profile', 'title', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('title',)
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'user__username',
        'title',
    )

    fieldsets = (
        ('Posts', {
            'fields': (('user', 'photo'))
        }),
        ('Extra info', {
            'fields': (
                ('title'), 
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
        }),
    )

    readonly_fields = ('created', 'modified', 'user')