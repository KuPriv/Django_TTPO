from django.contrib import admin


from .models import Parent, Children, Vaccination, VaccinationSchedule


class ParentModelAdmin(admin.ModelAdmin):
    list_display = ['contact_info']
    list_display_links = ['contact_info']
    search_fields = ['contact_info']

    class Meta:
        model = Parent


class ChildrenModelAdmin(admin.ModelAdmin):
    list_display = ['fio', 'birth', 'med_num', 'parent']
    list_display_links = ['fio', 'parent']
    list_filter = ['fio', 'birth', 'med_num', 'parent']
    search_fields = ['fio', 'birth', 'med_num', 'parent']

    class Meta:
        model = Children


class VaccinationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'introduction_schedule', 'contraindications', 'side_effects']
    list_display_links = ['name']
    search_fields = ['name', 'introduction_schedule', 'contraindications', 'side_effects']

    class Meta:
        model = Vaccination


class VaccinationScheduleModelAdmin(admin.ModelAdmin):
    list_display = ['child', 'vaccination', 'scheduled_date']
    list_display_links = ['child', 'vaccination']
    list_filter = ['child', 'vaccination', 'scheduled_date']
    search_fields = ['child', 'vaccination', 'scheduled_date']

    class Meta:
        model = VaccinationSchedule


admin.site.register(Children, ChildrenModelAdmin)
admin.site.register(Parent, ParentModelAdmin)
admin.site.register(Vaccination, VaccinationModelAdmin)
admin.site.register(VaccinationSchedule, VaccinationScheduleModelAdmin)