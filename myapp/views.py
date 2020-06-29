from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .CryptographyField import Cypher,ValidationError
from .forms import FileForm,DecryptForm
from .models import MyModel,DecryptModel

def home(request):
    return render(request, 'myapp/home.html')

def upload_files(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files_list')
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {
        'form': form
    })
    
def files_list(request):
    files = MyModel.objects.all()
    return render(request, 'file_list.html', {
        'files': files})
    
def encrypt_files(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                myfile = request.FILES.get('file', None)
                password = request.POST.get('password', None)
                encrypted_file = Cypher().encrypt_file(myfile, password, extension='enc')
                mymodel = MyModel.objects.create(file=encrypted_file)
                mymodel.save()
                return redirect('files_list')
            except ValidationError as e:
                print(e)
            
    else:
        form = FileForm()
    
    return render(request, 'upload_file.html', {'form': form})

def decrypt_files(request):
    if request.method == 'POST':
        form = DecryptForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                password = request.POST.get('password', None)
                mydoc = request.FILES.get('encryptedFile', None)
                decrypted_file = Cypher().decrypt_file(mydoc, password, extension='enc')
                decryptmodel=DecryptModel.objects.create(encryptedFile=decrypted_file)
                decryptmodel.save()
                return redirect('files_list')
            except ValidationError as e:
                print(e)
    else:
         form = FileForm()
    return render(request, 'upload_file.html', {'form': form})