from django.shortcuts import redirect , render
from .models import Employee
import uuid
from django.db.models import Sum

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def employee(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        salary = request.POST.get('salary')
        description = request.POST.get('description')
        emp_uuid = str(uuid.uuid4())
        print(id,f_name , l_name , salary , description)
        Employee.objects.create(first_name = f_name,
                                last_name = l_name,
                                salary = salary,
                                description = description,
                                emp_id = emp_uuid,
                                )
        return redirect('/')
    else:
        emp_obj =  Employee.objects.all()
        # emp_obj =  Employee.objects.filter(first_name__startswith = "an")
        # emp_obj =  Employee.objects.filter(salary = 120000)
        # emp_obj =  Employee.objects.filter(salary__gte = 10000,salary__lte = 20000)
        print(emp_obj)
        context = {'emp':emp_obj}
        return render(request, 'index.html',context) 
    
def deleteEmployee(request,id):
    empobj = Employee.objects.get(id = id)
    empobj.delete()
    return redirect("/") 

def updateEmployee(request,id):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        salary = request.POST.get('salary')
        description = request.POST.get('description')
        
        obj = Employee.objects.get(id = id)
        obj.first_name = f_name
        obj.last_name = l_name
        obj.salary = salary
        obj.description = description
        
        obj.save()        
        return redirect('/')
    else: 
        obj = Employee.objects.get(id = id)
        context = {'empobj':obj}
        return render(request, 'update.html',context) 
