# urls.py
from django.urls import path
from .views import (
    employee_create_view,
    AllEmployee,
    SeatchEmployee,
    getEducation,
    export_employees_to_excel,
    export_educations_to_excel,
    import_employees_from_excel,
    import_educations_from_excel
)

urlpatterns = [
    path("", employee_create_view, name="employee_create"),
    path("allEmployee/", AllEmployee.as_view(), name="all_employee"),
    path("search/", SeatchEmployee.as_view(), name="search_employee"),
    path("edu/<int:pk>/", getEducation, name="education"),
    path("export-employee/", export_employees_to_excel, name="exportEmployee"),
    path("export-edu/",export_educations_to_excel,name="exportEdu"),
    path("import-employee/",import_employees_from_excel,name="importEmployee"),
    path("import-edu/",import_educations_from_excel,name="importEdu")
]
