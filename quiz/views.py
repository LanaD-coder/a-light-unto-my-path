from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from question.models import Question, Answer
from result.models import Result

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/quiz_main.html'

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz/quizes.html', {'obj': quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,

    })

def save_quiz_view(request, pk):
    print(request.POST)

    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        questions = []
        data = dict(request.POST.lists())

        data.pop('csrfmiddlewaretoken', None)

        for key, values in data.items():
            print(f'🟡 Received Key: {key} | Values: {values}')


            question_text = key.replace("question-", "")

            try:

                question = Question.objects.get(text=question_text)
                questions.append(question)
                print(f'Found Question: {question.text}')

            except Question.DoesNotExist:
                print(f'Question Not Found: {question_text}')

        print(f'Final Question List: {questions}')

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results. append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})

        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'result': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'result': results})

    return JsonResponse({'error': 'Invalid request'}, status=400)

