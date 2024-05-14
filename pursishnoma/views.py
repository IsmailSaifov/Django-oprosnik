from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import Question, Choice, Response, MainQuestion
from django.db.models import Count, Min
import uuid

def survey(request):
    questions = Question.objects.all()
    main_questions = MainQuestion.objects.all()
    context = {'questions': questions, 'main_questions' : main_questions}
    return render(request, 'survey.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
    

def submitted_view(request):
    return render(request, 'submitted.html')

def submit_survey(request):
    if request.method == 'POST':
        try:
            # Генерация session_id
            if not request.session.session_key:
                request.session.save()
            # Session Handling
            session_id = uuid.uuid4().hex
            if not session_id:
                messages.error(request, 'Session ID not found.')
                return HttpResponseRedirect(reverse('survey'))

            # Client IP Address
            ip_address = get_client_ip(request)

            # Process Submitted Responses
            missed_questions = []
            for question in Question.objects.all():
                choice_key = f'choice_{question.id}'
                text_response_key = f'question_{question.id}_text_response'

                choice_value = request.POST.get(choice_key)
                text_response_value = request.POST.get(text_response_key)
                # Validate and Handle Responses
                if choice_value is not None and choice_value.isdigit():
                    try:
                        choice = Choice.objects.get(pk=choice_value)
                        Response.objects.create(
                            session_id=session_id, question=question, choice=choice, ip_address=ip_address,text_response=text_response_value
                        )
                    except Choice.DoesNotExist:
                        # Handle missing choice gracefully (e.g., log or display error message)
                        messages.error(request, f'Invalid choice for question: {question.question_text}')

                elif text_response_value is not None:  # Handle even empty text input
                    Response.objects.create(
                        session_id=session_id, question=question, text_response=text_response_value, ip_address=ip_address
                    )
                else:
                    missed_questions.append(question.question_text)
            for main_question in MainQuestion.objects.all():  # Assuming MainQuestion is your model for main questions
                for question in main_question.question_set.all():
                    choice_key = str(question.id)
                    choice_value = request.POST.get(choice_key)
                    if choice_value is not None and choice_value.isdigit():
                        try:
                            choice = Choice.objects.get(pk=choice_value)
                            Response.objects.create(
                                session_id=session_id,
                                question=question,
                                choice=choice,
                                ip_address=ip_address,
                                question_main=main_question
                            )
                        except Choice.DoesNotExist:
                            # Handle missing choice gracefully (e.g., log or display error message)
                            messages.error(
                                request, f'Invalid choice for question: {question.question_text}'
                            )
                    else:
                        missed_questions.append(question.question_text)
        except (Question.DoesNotExist, ValueError) as e:
            messages.error(request, str(e))
            return HttpResponseRedirect(reverse('survey'))

    return HttpResponseRedirect(reverse('submitted'))



def respons_list(request):
    # Группируем ответы по session_id и подсчитываем количество уникальных session_id
    unique_session_ids = Response.objects.values('session_id').annotate(cr_date=Min('cr_date'), count=Count('session_id'))

    context = {'unique_session_ids': unique_session_ids}
    return render(request, 'response_list.html', context)


def response_detail(request, session_id):
    # Получаем все ответы для выбранного session_id
    responses = Response.objects.filter(session_id=session_id)
    session_id = session_id
    
    context = {'responses': responses,'session_id': session_id}
    return render(request, 'response_detail.html', context)
