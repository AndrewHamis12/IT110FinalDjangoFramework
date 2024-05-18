
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render



def content_view(request):
    return render(request, 'content.html')


def landing_page(request):
    return render(request, 'profile.html')

def churches(request):
    return render(request, 'churches.html')

def devotional(request):
    return render(request, 'devotional.html')

def church(request):
    return render(request, 'church.html')
    
def devotionconts(request):
    return render(request, 'devotionconts.html')

def stories(request):
    return render(request, 'stories.html')

def news1(request):
    return render(request, 'news1.html')

def news2(request):
    return render(request, 'news2.html')

def news3(request):
    return render(request, 'news3.html')

def feedback(request):
    return render(request, 'feedback.html')

def content(request):
    return render(request, 'content.html')



def profile(request):
 user = request.user
 context = {'profile': profile}
 return render(request, 'profile.html', context)

@login_required
def profile(request):
 return render(request, 'content.html', {})

def logoutaccount(request):
  logout(request)
  return redirect('/accounts/login/')

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Church
from .forms import ChurchForm

def churches(request):
    churches = Church.objects.all()
    return render(request, 'churches.html', {'churches': churches})

def church_form(request):
    if request.method == 'POST':
        form = ChurchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/churches/')  # Redirect to the appropriate URL after form submission
    else:
        form = ChurchForm()
    return render(request, 'church_form.html', {'form': form})  # Corrected template path


def church_edit(request, pk):
    church = get_object_or_404(Church, pk=pk)
    if request.method == 'POST':
        form = ChurchForm(request.POST, instance=church)
        if form.is_valid():
            form.save()
            return redirect('/accounts/churches/')
    else:
        form = ChurchForm(instance=church)
    return render(request, 'church_edit.html', {'form': form})

def church_confirm_delete(request, pk):
    church = get_object_or_404(Church, pk=pk)
    if request.method == 'POST':
        church.delete()
        return redirect('/accounts/churches/')
    return render(request, 'church_confirm_delete.html', {'church': church})


def church(request):
    churches = Church.objects.all()  # Query all church objects from the database
    return render(request, 'church.html', {'churches': churches})


from django.views.generic import UpdateView

class ChurchEditView(UpdateView):
    model = Church
    form_class = ChurchForm
    template_name = 'church_edit.html'  # Update with your template name
    success_url = '/accounts/churches/'  # Update with your desired success URL

    def form_valid(self, form):
        # Any additional processing can be done here before saving the form
        return super().form_valid(form)


# views.py in your existing app
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/thank_you/')  # Redirect to thank you page after successful submission
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


def thank_you(request):
    return render(request, 'thank_you.html')

def feedback_list(request):
    return render(request, 'feedback_list.html')


# views.py in your app
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Feedback

class FeedbackListView(ListView):
    model = Feedback
    template_name = 'feedback_list.html'
    context_object_name = 'feedbacks'

class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'feedback_detail.html'
    context_object_name = 'feedback'

class FeedbackDeleteView(DeleteView):
    model = Feedback
    template_name = 'feedback_confirm_delete.html'
    success_url = reverse_lazy('feedback_list')


  

