from django.shortcuts import render
from .models import StudentDetail

# Create your views here.
def addNew(request):
	return render(request,'details/addNewData.html')

def addData(request):
	obj = StudentDetail()
	obj.name = request.POST.get('name')
	obj.subject = request.POST.get('subject')
	obj.save()
	obj1 = StudentDetail.objects.all()
	return render(request,'details/firstDisp.html',{'Data':obj1})

def dispAll(request):
	obj = StudentDetail.objects.all().order_by('name')
	return render(request,'details/firstDisp.html',{'Data':obj})

def editData(request):
	ref_id = request.GET.get('id')
	print(ref_id)
	obj = StudentDetail.objects.get(id=ref_id)
	displayed_data = {'id':obj.id , 'name':obj.name , 'subject':obj.subject}
	return render(request,'details/editData.html',displayed_data)


def editNewData(request):
	ref_id = request.POST.get('id')
	print(ref_id)
	#ref_name = request.POST.get('name') ; ref_sub = request.POST.get('subject')
	obj = StudentDetail.objects.get(id=ref_id)
	obj.name = request.POST.get('name')
	obj.subject = request.POST.get('subject')
	obj.save()
	newData = StudentDetail.objects.all()
	return render(request,'details/firstDisp.html',{'Data':newData})

def deleteData(request):
	ref_id = request.GET.get('id')
	print(ref_id)
	obj = StudentDetail.objects.get(id=ref_id)
	obj.delete()
	newData = StudentDetail.objects.all()
	return render(request,'details/firstDisp.html',{'Data':newData})
