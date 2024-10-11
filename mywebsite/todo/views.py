from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
  data =dict(
    name ='Ade Nuryana',
    kelas ='10 ipa'
  )
  
  return render(request, 'todo/index.html', data)
