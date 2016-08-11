from django.shortcuts import render_to_response
# Create your views here.
# sutdent list

def  table(request):
    students = {'Jack': [22, 'boy', 'Programmer'],
                'Alen': [27, 'boy', 'Designer'],
                'Una': [23, 'girl', 'Tester'],
                'Brant': [23, 'girl', 'Tester'],
                'David': [23, 'boy', 'Tester']}
    return render_to_response('table.html', {'student_list': students})