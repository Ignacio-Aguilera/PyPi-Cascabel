# Cascabel


Cascabel es un proyecto desarrollado principalmente para la agilizacion en la creación de paginas web mediantes el Framework de flask y librerias asociadas (Actualmente _**Flask SqlAlchemy**_ y _**Flask WTF**_ )

Crear un nuevo projecto:

```bash
# Ubiquémonos en la carpeta donde quieras crear el proyecto.
C:\Users\User\Desktop> cascabel --new_project project_name
```

Ejecutar proyecto:

```bash
# Ubiquémonos en la carpeta del proyecto.
C:\Users\User\Desktop\project_name> python execute.py
```

Crear controlador:

```bash
# Ubiquémonos en la carpeta del proyecto.
C:\Users\User\Desktop\project_name> cascabel --make_controller project_name
```

Crear controlador CRUD:

```bash
# Ubiquémonos en la carpeta del proyecto.
C:\Users\User\Desktop\project_name> cascabel --make_crud_controller project_name
```

Crear modelo:

```bash
# Ubiquémonos en la carpeta del proyecto.
C:\Users\User\Desktop\project_name> cascabel --make_model project_name
```

Crear Request:

```bash
# Ubiquémonos en la carpeta del proyecto.
C:\Users\User\Desktop\project_name> cascabel --make_request project_name
```


Consultar comandos

```bash
cascabel --help
```

Listado de comandos:
| Comando extendido | Abreviación | 
| -- | -- |
| --help | -h |
| --verify_libraries | -vl |
| --new_project | -np |
| --make_controller | -mc |
| --make_crud_controller | -mcc |
| --make_model | -mm |
| --make_request | -mr |





Observaciones: _Cascabel actualmente se encuentra bajo desarrollo, esto puede generar que la creación de plantillas en futuras versiones no sean compatibles con las actuales._
