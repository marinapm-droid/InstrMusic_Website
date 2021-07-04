import matplotlib
from django.contrib.auth import authenticate, login, logout
from django.db.models import Avg
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

matplotlib.use('Agg')
import matplotlib.pyplot as plt

from .models import Contact, Comment, Quizz, Event, Musician
from .forms import ContactForm, MusicianForm, QuizzForm, CommentForm, Result_QuizzForm, EventForm


def home_page_view(request):  # para renderizar a página home.html teremos a função home_page_view
    if request.user.is_authenticated:
        return render(request, "website/home.html", {
            'message': "logged"
        })
    return render(request, 'website/home.html')


def about_page_view(request):
    if request.user.is_authenticated:
        return render(request, "website/about.html", {
            'message': "logged"
        })
    return render(request, 'website/about.html')


def spa_page_view(request):
    if request.user.is_authenticated:
        return render(request, "website/spa.html", {
            'message': "logged"
        })
    return render(request, 'website/spa.html')


def section(request, num):
    if num == 1:
        return render(request, 'website/article_1.html')
    elif num == 2:
        return render(request, 'website/article_2.html')
    elif num == 3:
        return render(request, 'website/article_3.html')
    elif num == 4:
        return render(request, 'website/article_4.html')
    else:
        raise Http404("No such section")


def instructions_page_view(request):
    if request.user.is_authenticated:
        return render(request, "website/instructions.html", {
            'message': "logged"
        })
    return render(request, 'website/instructions.html')


def faq_page_view(request):
    if request.user.is_authenticated:
        return render(request, "website/faq.html", {
            'message': "logged"
        })
    return render(request, 'website/faq.html')


def download_page_view(request):
    if request.user.is_authenticated:
        return render(request, "website/download.html", {
            'message': "logged"
        })
    return render(request, 'website/download.html')


def about_website_page_view(request):
    if request.user.is_authenticated:
        return render(request, "website/about_website.html", {
            'message': "logged"
        })
    return render(request, 'website/about_website.html')


def about_page_view(request):
    if request.user.is_authenticated:
        return render(request, "website/about.html", {
            'message': "logged"
        })
    return render(request, 'website/about.html')


def list_contact_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('website:login'))
    context = {'contacts': Contact.objects.all(), 'message': "logged"}
    return render(request, 'website/list_contact.html', context)


def contact_us_page_view(request):
    form = ContactForm(request.POST or None)

    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('website:contact_us'))
        context = {'form': form, 'message': "logged"}
        return render(request, "website/contact_us.html", context)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:contact_us'))

    context = {'form': form}

    return render(request, 'website/contact_us.html', context)


def edit_contact_page_view(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    form = ContactForm(request.POST or None, instance=contact)

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('website:login'))

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:list_contact'))

    context = {'form': form, 'contact_id': contact_id, 'message': "logged"}
    return render(request, 'website/edit_contact.html', context)


def remove_contact_page_view(request, contact_id):
    Contact.objects.get(id=contact_id).delete()
    return HttpResponseRedirect(reverse('website:list_contact'))


def events_page_view(request):
    context = {'events': Event.objects.all()}

    if not request.user.is_authenticated:
        return render(request, 'website/events.html', context)

    context = {'events': Event.objects.all(), 'message': "logged"}

    return render(request, "website/events.html", context)


def events_detail_page_view(request, events_id):
    e = Event.objects.all().get(id=events_id)

    if request.user.is_authenticated:
        context = {'events': e,
                   'musicians': e.Musician.all(),
                   'non_musicians': Musician.objects.exclude(event=e), 'message': "logged"}
        return render(request, 'website/events_details.html', context)

    context = {'events': e,
               'musicians': e.Musician.all(),
               'non_musicians': Musician.objects.exclude(event=e)}

    return render(request, 'website/events_details.html', context)


def participate_page_view(request, events_id):
    e = Event.objects.get(id=events_id)
    form = MusicianForm(request.POST or None)

    if request.user.is_authenticated:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            obj.event.add(e)

            return HttpResponseRedirect(reverse('website:events_details', args=(e.id,)))
        context = {'form': form, 'e': e, 'events_id': events_id, 'message': "logged"}
        return render(request, 'website/participate.html', context)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        obj.event.add(e)
        return HttpResponseRedirect(reverse('website:events_details', args=(e.id,)))

    context = {'form': form, 'e': e, 'events_id': events_id}
    return render(request, 'website/participate.html', context)


def login_page_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('website:list_contact'))
        else:
            return render(request, "website/login.html", {
                'message': "Invalid credentials :("
            })
    return render(request, "website/login.html")


def logout_page_view(request):
    logout(request)
    return render(request, "website/login.html")


def comments_page_view(request):
    form = CommentForm(request.POST or None)

    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('website:result_comment'))
        context = {'form': form, 'message': "logged"}
        return render(request, 'website/comments.html', context)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:result_comment'))

    context = {'form': form}
    return render(request, 'website/comments.html', context)


def comment_results_page_view(request):
    c = Comment.objects.all()
    exp_vals_1 = [Comment.objects.filter(question1='Yes').count(), Comment.objects.filter(question1='No').count(),
                  Comment.objects.filter(question1='More or Less').count()]
    exp_labels_1 = ["Yes", "No", "More or Less"]
    plt.bar(exp_labels_1, exp_vals_1)
    plt.title("Did you enjoy the website?")
    plt.savefig('website/static/website/images/media1_plot.png')
    plt.clf()

    exp_vals_2 = [Comment.objects.filter(question5='Yes').count(), Comment.objects.filter(question5='No').count()]
    exp_labels_2 = ["Yes", "No"]
    plt.bar(exp_labels_2, exp_vals_2)
    plt.title("Did you find any bugs?")
    plt.savefig('website/static/website/images/media2_plot.png')
    plt.clf()

    exp_vals_3 = [Comment.objects.aggregate(Avg('question3'))['question3__avg'],
                  Comment.objects.aggregate(Avg('question4'))['question4__avg'],
                  Comment.objects.aggregate(Avg('question2'))['question2__avg'],
                  Comment.objects.aggregate(Avg('question6'))['question6__avg'],
                  Comment.objects.aggregate(Avg('question8'))['question8__avg']]
    exp_labels_3 = ["Q3", "Q4", "Q5", "Q6", "Q8"]
    plt.bar(exp_labels_3, exp_vals_3)
    plt.title("Avg Comments")
    plt.savefig('website/static/website/images/media3_plot.png')
    plt.clf()

    return render(request, 'website/result_comment.html')


def quizz_results_page_view(request):
    q = Quizz.objects.latest('id')
    form = Result_QuizzForm()
    obj = form.save(commit=False)

    # cotação 2 cada pergunta
    evaluation = 0
    # question1
    if str(q.question1).lower() == "yes":
        evaluation += 2
        obj.result_question1 = 2
    # question2
    if str(q.question2).lower() == "instrmusic":
        evaluation += 2
        obj.result_question2 = 2
    # question3
    if str(q.question3).lower() == "3":
        evaluation += 2
        obj.result_question3 = 2
    # question4
    if str(q.question4).lower() == "yes":
        evaluation += 2
        obj.result_question4 = 2
    # question5
    if str(q.question5).lower() == "yes":
        evaluation += 2
        obj.result_question5 = 2
    # question6
    if str(q.question6).lower() == "4":
        evaluation += 2
        obj.result_question6 = 2
    # question7
    if str(q.question7).lower() == "yes":
        evaluation += 2
        obj.result_question7 = 2
    # question8
    if str(q.question8).lower() == "1":
        evaluation += 2
        obj.result_question8 = 2
    # question9
    if str(q.question9).lower() == "2":
        evaluation += 2
        obj.result_question9 = 2
    # question10
    if str(q.question10).lower() == "2020":
        evaluation += 2
        obj.result_question10 = 2

    obj.final_result = evaluation
    obj.quizz = q
    obj.save()

    exp_vals = [obj.result_question1, obj.result_question2, obj.result_question3, obj.result_question4,
                obj.result_question5, obj.result_question6, obj.result_question7, obj.result_question8,
                obj.result_question9, obj.result_question10]
    exp_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    plt.bar(exp_labels, exp_vals)
    plt.title("Results")
    plt.savefig('website/static/website/images/my_plot.png')

    if request.user.is_authenticated:
        context = {'quizz': q, 'quizz_results': obj, 'message': "logged"}

    return render(request, "website/quizz_results.html", context)


def quizz_page_view(request):
    form = QuizzForm(request.POST or None)

    if request.user.is_authenticated:
        form.email = "m@gmail.com"
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('website:quizz_results'))
        context = {'form': form, 'message': "logged"}
        return render(request, 'website/quizz.html', context)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:quizz_results'))

    context = {'form': form}
    return render(request, 'website/quizz.html', context)


def new_event_page_view(request):
    form = EventForm(request.POST or None)

    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('website:events'))
        context = {'form': form, 'message': "logged"}
        return render(request, "website/new_event.html", context)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:events'))

    context = {'form': form}

    return render(request, 'website/new_event.html', context)


def article_1(request):
    if request.user.is_authenticated:
        return render(request, "website/article_1.html", {
            'message': "logged"
        })
    return render(request, 'website/article_1.html')


def article_2(request):
    if request.user.is_authenticated:
        return render(request, "website/article_2.html", {
            'message': "logged"
        })
    return render(request, 'website/article_2.html')


def article_3(request):
    if request.user.is_authenticated:
        return render(request, "website/article_3.html", {
            'message': "logged"
        })
    return render(request, 'website/article_3.html')


def article_4(request):
    if request.user.is_authenticated:
        return render(request, "website/article_4.html", {
            'message': "logged"
        })
    return render(request, 'website/article_4.html')
