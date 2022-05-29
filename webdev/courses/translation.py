from modeltranslation.translator import register, TranslationOptions
from .models import Course, Theme, QuestionParent, Question

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields=("title", "description")
    
@register(Theme)
class ThemeTranslationOptions(TranslationOptions):
    fields=("first_title", "first_text", 'second_title', 'second_text', 'third_title', "third_text")
    
@register(QuestionParent)
class QuestionParentTranslationOptions(TranslationOptions):
    fields=("title",)
    
@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields=("question", "option1", "option2", "option3", "option4")
    
    