from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Contact, Comment, Quizz, Event, Location, Musician
from .forms import ContactForm, MusicianForm, QuizzForm, CommentForm


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


def instructions_page_view(request):
    if request.user.is_authenticated:
        return render(request, "website/about.html", {
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
        context = {'form': form, 'events_id': events_id, 'message': "logged"}
        return render(request, 'website/participate.html', context)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        obj.event.add(e)
        return HttpResponseRedirect(reverse('website:events_details', args=(e.id,)))

    context = {'form': form, 'events_id': events_id}
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
        context = {'form': form, 'message': "logged"}
        return render(request, "website/comments.html", context)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:comments'))

    context = {'form': form}

    return render(request, 'website/comments.html', context)


def quizz_results_page_view(request, quizz_id):
    q = Quizz.objects.all().get(id=quizz_id)
    context = {'quizz': q}
    return render(request, "website/quizz_results.html", context)


def quizz_page_view(request):
    form = QuizzForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:quizz_results.html', args=(form.id,)))

    context = {'form': form}

    return render(request, 'website/quizz.html', context)
