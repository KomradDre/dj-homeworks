from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    ordering = request.GET.get('ordering', 'group')

    if ordering not in ['group', 'name']:
        ordering = 'group'

    # Получаем всех студентов с предзагрузкой учителей и сортируем
    students = Student.objects.prefetch_related('teachers').order_by(ordering)

    context = {
        'object_list': students,
        'ordering': ordering
    }

    return render(request, template, context)