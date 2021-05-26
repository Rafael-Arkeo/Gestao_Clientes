from django.shortcuts import render,redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required

@login_required()
def clientes_page(request):
    person = Person.objects.all()
    return render(request, 'index.html',{'person':person})
@login_required()
def novo_cliente(request):
    form = PersonForm(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect('list-cli')
    return render(request, 'formulario_clientes.html',{'form':form})

@login_required()
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('list-cli')
    return render(request, 'person_update.html', {'form':form})
@login_required()
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=person)
    if request.method == 'POST':
        person.delete()
        return redirect('list-cli')
    return render(request, 'person_delete.html',{'person':person})