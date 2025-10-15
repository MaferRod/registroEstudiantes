import requests
from django.shortcuts import render, redirect

API_URL = 'http://127.0.0.1:5000/students'

# Funciones auxiliares
def fetch_students():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException:
        pass
    return []

def fetch_student(student_id):
    try:
        response = requests.get(f"{API_URL}/{student_id}")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException:
        pass
    return None

def create_student(data):
    try:
        return requests.post(API_URL, json=data)
    except requests.exceptions.RequestException:
        return None

def update_student(student_id, data):
    try:
        return requests.put(f"{API_URL}/{student_id}", json=data)
    except requests.exceptions.RequestException:
        return None

def remove_student(student_id):
    try:
        requests.delete(f"{API_URL}/{student_id}")
    except requests.exceptions.RequestException:
        pass

# Vistas
def student_list(request):
    students = fetch_students()
    return render(request, 'students/list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name', ''),
            'age': int(request.POST.get('age', 0)),
            'email': request.POST.get('email', '')
        }
        create_student(data)
        return redirect('student_list')
    return render(request, 'students/add.html')

def edit_student(request, student_id):
    student = fetch_student(student_id)
    if not student:
        return redirect('student_list')

    if request.method == 'POST':
        data = {
            'name': request.POST.get('name', ''),
            'age': int(request.POST.get('age', 0)),
            'email': request.POST.get('email', '')
        }
        response = update_student(student_id, data)
        if response and response.status_code == 200:
            return redirect('student_list')
        else:
            return render(request, 'students/edit.html', {'student': data, 'error': 'No se pudo actualizar el estudiante'})

    return render(request, 'students/edit.html', {'student': student})

def delete_student(request, student_id):
    remove_student(student_id)
    return redirect('student_list')
