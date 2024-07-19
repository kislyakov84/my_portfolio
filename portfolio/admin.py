from django.contrib import admin
from .models import Skill, Author, Category, Testimony, Work, Service, Message


admin.site.register(Category)
admin.site.register(Testimony)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Author)
admin.site.register(Work)
admin.site.register(Message)
