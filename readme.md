
<img src="https://github.com/Ignacio-Aguilera/PyPi-Cascabel/blob/main/cascabel.png?raw=True" alt="cascabel" height="72" width="343"/> 
 
___


Cascabel es un proyecto desarrollado principalmente con el propósito de agilizar la creación de páginas web mediante el uso del framework Flask y sus librerias asociadas (_**Flask SqlAlchemy**_ y _**Flask WTF**_).


## Listado de comandos:
| Comando extendido | Abreviación | 
| -- | -- |
| --help | -h |
| --verify_libraries | -vl |
| --new_project | -np |
| --make_controller | -mc |
| --make_crud_controller | -mcc |
| --make_model | -mm |
| --make_request | -mr |

## Uso de comandos:


Para el uso de los comandos se pueden realizar de las siguientes maneras:

🪟 Windows:
```bash
C:\Users\User\Desktop> cascabel ...
C:\Users\User\Desktop> python -m cascabel ...
```

🐧 Linux:
```shell
xxxxx@xxxxx:~$ python -m cascabel ...
```

🍎 MacOS:
```shell
xxxxx@xxxxx ~ % python -m cascabel ...
```

### Estructura de comandos:

Crear un nuevo proyecto:

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

⚠️ _**Cascabel** se encuentra actualmente en fase de desarrollo, lo que podría resultar en la incompatibilidad entre las plantillas de las versiones futuras y las actuales._


