from django.contrib import admin
from .models import Course, Theme, Question, QuestionParent
from modeltranslation.admin import TranslationAdmin

# Register your models here.
class courseAdmin(TranslationAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {'slug':('title',)}
    
class themeAdmin(TranslationAdmin):
    list_display = ("first_title", "course")
    prepopulated_fields = {'slug':('first_title',)}
    
class quizParentAdmin(TranslationAdmin):
    list_display = ("title",)
    prepopulated_fields = {'slug': ('title',)}
    
class quiz(TranslationAdmin):
    list_diplay = ('parent',)
    
admin.site.register(Course, courseAdmin)
admin.site.register(Theme, themeAdmin)
admin.site.register(QuestionParent, quizParentAdmin)
admin.site.register(Question, quiz)