from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,'home.html',{'name':'Jahanzaib'})


def add(request):
  val1=request.POST['Num1']
  val2=request.POST['Num2']
  total=int(val1)+int(val2)
  return render(request,'result.html',{'result':total})