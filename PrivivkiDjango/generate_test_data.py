import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PrivivkiDjango.settings')
django.setup()

from Privivki.models import Children, Vaccination, VaccinationSchedule


def create_children(count):
    children = []
    for i in range(count):
        child = Children(
            fio=f'Ребенок {i}',
            birth=datetime.now() - timedelta(days=random.randint(0, 2000)),
            med_num=i,
            parent_id=1  # рродитель с ID=1
        )
        children.append(child)
    Children.objects.bulk_create(children)


def create_vaccinations():
    vaccinations = []
    for i in range(10):  # Создадим 10 различных прививок
        vaccination = Vaccination(
            name=f'Вакцина {i}',
            introduction_schedule=datetime.now() - timedelta(days=random.randint(0, 1000)),
            contraindications='Нет',
            side_effects='Нет'
        )
        vaccinations.append(vaccination)
    Vaccination.objects.bulk_create(vaccinations)


def create_vaccination_schedules(child_count, schedule_count):
    children = list(Children.objects.all()[:child_count])
    vaccinations = list(Vaccination.objects.all())
    schedules = []
    for _ in range(schedule_count):
        child = random.choice(children)
        vaccination = random.choice(vaccinations)
        schedule = VaccinationSchedule(
            child=child,
            vaccination=vaccination,
            scheduled_date=datetime.now() + timedelta(days=random.randint(0, 365))
        )
        schedules.append(schedule)
    VaccinationSchedule.objects.bulk_create(schedules)


if __name__ == '__main__':
    # Очистим существующие данные
    VaccinationSchedule.objects.all().delete()
    Children.objects.all().delete()
    Vaccination.objects.all().delete()

    # Создадим данные
    child_count = 1000  # Общее количество детей
    create_children(child_count)
    create_vaccinations()

    # Генерация данных для тестирования
    data_sizes = [10, 50, 100, 500, 1000]
    for size in data_sizes:
        print(f'Генерация {size} записей VaccinationSchedule...')
        create_vaccination_schedules(child_count, size)
        print('Готово!')