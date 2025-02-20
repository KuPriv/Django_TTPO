from django.db import models


class Parent(models.Model):
    contact_info = models.CharField(max_length=100, default="", verbose_name='контактная информация')

    def __unicode__(self):
        return self.contact_info

    def __str__(self):
        return self.contact_info

    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'


class MedicalStaff(models.Model):
    fio = models.CharField(max_length=50, default="", verbose_name='ФИО')
    job_title_choice = (
        ('Врач', 'Врач'),
        ('Медсестра', 'Медсестра'),
        ('Администратор', 'Администратор'),
    )

    job_title = models.CharField(max_length=25, default="", choices=job_title_choice)

    def __unicode__(self):
        return self.fio

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Медицинский работник'
        verbose_name_plural = 'Медицинские работники'


class Children(models.Model):
    fio = models.CharField(max_length=50, default="", verbose_name='ФИО')
    birth = models.DateField()
    med_num = models.IntegerField(unique=True, null=True, blank=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.fio

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'


class Vaccination(models.Model):
    name = models.CharField(max_length=50, default="", verbose_name='прививка')
    introduction_schedule = models.DateField()
    contraindications = models.TextField()
    side_effects = models.TextField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вакцина'
        verbose_name_plural = 'Вакцины'


class VaccinationLog(models.Model):
    vaccination = models.ForeignKey(Vaccination, on_delete=models.CASCADE)
    vaccination_date = models.DateField()
    type_vaccination = models.CharField(max_length=25)
    dosage = models.CharField(max_length=50)
    med_staff = models.ForeignKey(MedicalStaff, on_delete=models.SET_NULL, null=True, blank=True)

    def __unicode__(self):
        return self.vaccination

    def __str__(self):
        return self.vaccination

    class Meta:
        verbose_name = 'Журнал прививок'
        verbose_name_plural = 'Журнал прививок'


class Notification(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    message = models.TextField()
    date_of_send = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return f'Увдеомление для: {self.parent} от {self.date_of_send}'

    def __str__(self):
        return f'Увдеомление для: {self.parent} от {self.date_of_send}'

    class Meta:
        verbose_name = 'уведомление'
        verbose_name_plural = 'уведомления'


class Report(models.Model):
    med_staff = models.ForeignKey(MedicalStaff, on_delete=models.CASCADE)
    content = models.TextField()
    date_of_generation = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return f'Отчёт {self.med_staff} от {self.date_of_generation}'

    def __str__(self):
        return f'Отчёт {self.med_staff} от {self.date_of_generation}'

    class Meta:
        verbose_name = 'отчет'
        verbose_name_plural = 'отчёты'


class Report(models.Model):
    med_staff = models.ForeignKey(MedicalStaff, on_delete=models.CASCADE)
    content = models.TextField()
    date_of_generation = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return f'Отчёт {self.med_staff} от {self.date_of_generation}'

    def __str__(self):
        return f'Отчёт {self.med_staff} от {self.date_of_generation}'

    class Meta:
        verbose_name = 'отчет'
        verbose_name_plural = 'отчёты'


class VaccinationSchedule(models.Model):
    child = models.ForeignKey(Children, on_delete=models.CASCADE, verbose_name='Ребенок')
    vaccination = models.ForeignKey(Vaccination, on_delete=models.CASCADE, verbose_name='Прививка')
    scheduled_date = models.DateField(verbose_name='Дата проведения')

    def __unicode__(self):
        return f'Вакцинация {self.child} - {self.vaccination} {self.scheduled_date}'

    def __str__(self):
        return f'Вакцинация {self.child} - {self.vaccination} {self.scheduled_date}'

    class Meta:
        verbose_name = 'График вакцинации'
        verbose_name_plural = 'График вакцинаций'


class MedicalCard(models.Model):
    child = models.OneToOneField(Children, on_delete=models.CASCADE, primary_key=True)
    medical_story = models.TextField()
    current_health_status = models.TextField()

    def __unicode__(self):
        return f'Карточка: {self.child}'

    def __str__(self):
        return f'Карточка: {self.child}'

    class Meta:
        verbose_name = 'Медицинская карточка'
        verbose_name_plural = 'Медицинская карточка'