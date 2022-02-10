from django.db import models

# Create your models here.
class Student(models.Model):
    def __str__(self):
        if not self.nombre is None and not self.apellidos is None: 
            return self.nombre + " " + self.apellidos + " (CI:" + self.ci + ")"

        return "CI: " + self.ci + ")"

    ci = models.CharField(max_length = 50,  help_text = "CI")
    nombre = models.CharField(max_length = 200, help_text = "Nombre")
    apellidos = models.CharField(max_length = 200, help_text = "Apellidos")
    pais = models.CharField(max_length = 200, help_text = "País", null = True, blank = True)
    provincia = models.CharField(max_length = 200, null = True, help_text = "Provincia", blank = True)
    municipio = models.CharField(max_length = 200, null = True, help_text = "Municipio", blank = True)
    situacion_academica = models.CharField(max_length = 200, null = True, help_text = "Situación Académica", blank = True)
    estado = models.CharField(max_length = 200, null = True, help_text = "Estado", blank = True)
    direccion = models.CharField(max_length = 1000, null = True, help_text = "Dirección", blank = True)
    fecha_nacimiento = models.DateField("Fecha de Nacimiento", null = True, blank = True)
    carrera = models.CharField(max_length = 500, help_text = "Carrera", null = True, blank = True)
    facultad = models.CharField(max_length = 200, help_text = "Facultad", null = True, blank = True)
    tipo_curso = models.CharField(max_length = 200, help_text = "Tipo de curso", null = True, blank = True)
    correo = models.CharField(max_length = 200, help_text = "Correo electrónico", null = True, blank = True)
    fuente_ingreso = models.CharField(max_length = 200, help_text = "Fuente de Ingreso", null = True, blank = True)
    origen_academico = models.CharField(max_length = 200, help_text = "Origen Académico", null = True, blank = True)
    regimen_estudio = models.CharField(max_length = 200, help_text = "Regimen de Estudio", null = True, blank = True)
    natural_de = models.CharField(max_length = 200, help_text = "Natural de", null = True, blank = True)
    telefono = models.CharField(max_length = 200, help_text = "Teléfono", null = True, blank = True)
    fecha_ingreso = models.DateField("Fecha de Ingreso a la ES", null = True, blank = True)
    estado_civil = models.CharField(max_length = 200, help_text = "Estado Civil", null = True, blank = True)
    organizacion_politica = models.CharField(max_length = 200, help_text = "Organización política", null = True, blank = True)
    fecha_ingreso_ces = models.DateField("Fecha de ingreso al Ces", null = True, blank = True)
    fecha_matricula = models.DateField("Fecha de matrícula", null = True, blank = True)
    sexo = models.CharField(max_length = 200, help_text = "Sexo", null = True, blank = True)
    color_piel = models.CharField(max_length = 200, help_text = "Color de la piel", null = True, blank = True)
    tipo_estudiante = models.CharField(max_length = 200, help_text = "Tipo de estudiante", null = True, blank = True)
    anho_estudio = models.IntegerField(help_text = "Año de Estudio", null = True, blank = True)
    centro_trabajo = models.CharField(max_length = 200, help_text = "Centro de Trabajo", null = True, blank = True)
    nombre_padre = models.CharField(max_length = 500, help_text = "Nombre del Padre", null = True, blank = True)
    nivel_academico_padre = models.CharField(max_length = 200, help_text = "Nivel Academico del Padre", null = True, blank = True)
    nombre_madre = models.CharField(max_length = 500, help_text = "Nombre de la Madre", null = True, blank = True)
    nivel_academico_madre = models.CharField(max_length = 200, help_text = "Nivel academico de la madre", null = True, blank = True)
    tipo_servicio_militar = models.CharField(max_length = 200, help_text = "Tipo de servicio militar", null = True, blank = True)
    edad = models.IntegerField("Edad", null = True, blank = True)