from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactEntry

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # You can redirect to a thank-you page
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def contact_entries_view(request):
    entries = ContactEntry.objects.all()
    return render(request, 'contact_entries.html', {'entries': entries})



from django.shortcuts import get_object_or_404, redirect
from .forms import ContactEntryForm

def update_contact(request, pk):
    contact = get_object_or_404(ContactEntry, pk=pk)
    if request.method == 'POST':
        form = ContactEntryForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_entries')
    else:
        form = ContactEntryForm(instance=contact)
    
    return render(request, 'update_contact.html', {'form': form})

def delete_contact(request, pk):
    contact = get_object_or_404(ContactEntry, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_entries')
