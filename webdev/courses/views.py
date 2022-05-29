from django.shortcuts import render
from .models import Course, Theme, Question, QuestionParent

# Create your views here.
def home(request):
    return render(request, "home.html")

def courses(request):
    coursy = Course.objects.all()
    return render(request, "courses.html", {'courses':coursy})

def contact(request):
    return render(request, "contact.html")

def themes_of_course(request, slug):
    course = Course.objects.get(slug=slug)
    themes = Theme.objects.filter(course=course.id)
    return render(request, "themes_of_course.html", {'themes':themes, 'course':course})

def theme(request, slugCourse, slugTheme):
    course = Course.objects.get(slug = slugCourse)
    theme = Theme.objects.get(slug=slugTheme)
    quiz = QuestionParent.objects.all().filter(theme = theme)
    return render(request, "theme.html", {'theme':theme, 'course':course, "quiz": quiz})

def quiz(request, slugCourse, slugTheme, slugQuiz):
    course = Course.objects.get(slug = slugCourse)
    theme = Theme.objects.get(slug = slugTheme)
    parent = QuestionParent.objects.get(slug = slugQuiz)
    questions = Question.objects.all().filter(parent = parent)
    checked = {}
    results = []
    
    counter = 1
    for q in questions:
        q.question = f"{counter}) {q.question}"
        results.append(q.answer)
        print(q.answer)
        counter+=1
        
    print(len(questions))
    return render(request, "test.html", {"course":course, "theme": theme, "questions": questions, "parent": parent, "results": results, "checked":checked})