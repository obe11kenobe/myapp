from django.http import JsonResponse
from django.shortcuts import render
import json
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

def hello(request):
    return render(request, 'hello.html')

def get_employees(request):
    # Получение списка сотрудников через raw-SQL
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, full_name, gender, age, position, category FROM employees")
        rows = cursor.fetchall()
    employees = [
        {'id': row[0], 'full_name': row[1], 'gender': row[2], 'age': row[3], 'position': row[4], 'category': row[5]}
        for row in rows
    ]
    print("Список сотрудников:", employees)  # Отладочный вывод
    return JsonResponse({'employees': employees})

@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        full_name = data.get('full_name')
        gender = data.get('gender')
        age = data.get('age')
        position = data.get('position')
        category = data.get('category')
        print(f"Добавление сотрудника: {full_name}, {gender}, {age}, {position}, {category}")  # Отладочный вывод
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO employees (full_name, gender, age, position, category) VALUES (%s, %s, %s, %s, %s)",
                [full_name, gender, age, position, category]
            )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def update_employee_position(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        employee_id = data.get('id')
        position = data.get('position')
        print(f"Обновление должности: id={employee_id}, position={position}")  # Отладочный вывод
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE employees SET position = %s WHERE id = %s",
                [position, employee_id]
            )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def delete_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        employee_id = data.get('id')
        print(f"Удаление сотрудника: id={employee_id}")  # Отладочный вывод
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM employees WHERE id = %s", [employee_id])
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)