from django.shortcuts import render, HttpResponseRedirect
from .models import Student
from .forms import StudentForm

# Create your views here.


# this function for add and show details
def showstudents(request):
    frmm = StudentForm()
    if request.method == 'POST':
        frmm = StudentForm(request.POST, request.FILES)
        if frmm.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # phone = form.cleaned_data['phone']
            # student = Student(name=name,email=email,phone=phone,)
            # student.save()
            frmm.save()
            frmm = StudentForm()
    else:
        frmm = StudentForm()
    showfrmm = Student.objects.all()            
  
    context = {'form':frmm, 'showform':showfrmm}
    return render(request, 'CrudPractice/showstudents.html', context)


# this function for delete details
def deletestudents(request, id):
    if request.method == 'POST':
        delfrmm = Student.objects.get(pk=id)
        delfrmm.delete()
    return HttpResponseRedirect('/')


# this function for edit the details

def editstudents(request, id):

    if request.method == 'POST':
        geteditid = Student.objects.get(pk=id)
        efrmm = StudentForm(request.POST, instance=geteditid)
        if efrmm.is_valid():
            efrmm.save()
    else:
        geteditid = Student.objects.get(pk=id)
        efrmm = StudentForm(instance=geteditid)
    editcontext = {'editform':efrmm}
    return render(request, 'CrudPractice/editstudents.html', editcontext)
    # return render(request, 'CrudPractice/editstudents.html',{'id':id})