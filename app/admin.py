from django.contrib import admin
from . models import User,Candidate,UserProfile,Like,Section

# Register your models here.

admin.site.register(User)
admin.site.register(Candidate)
admin.site.register(UserProfile)
admin.site.register(Like)
admin.site.register(Section)