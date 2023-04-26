# Cascabel



Desarrollado por Ignacio Aguilera Oyaneder.

## Ejemplos de uso (Versión Alpha)

Crear un nuevo projecto

```bash
# Dirigete a la carpeta en la que desees crear el projecto.
C:\Users\User\Desktop> cascabel --new_project project_name
```

Consultar comandos

```bash
cascabel --help
```

Abreviaciones de comandos:
| Comando extendido | Abreviación | 
| -- | -- |
| verify_libraries | vl |
| install_libraries | il |
| new_project | n |
| make_controller | co |




commands = {
    "install_libraries"  : ["--install_libraries", "-il"],
    "verify_libraries"   : ["--verify_libraries" , "-vl"],

    "new_project"        : ["--new_project"      , "-new", "-n"],
    "make_controller"    : ["--make_controller"  , "-co"],
    "make_manager_controller" : ["--make_manager_controller"  , "-mco"],
    "make_database"      : ["--make_database"       , "-da"],
    "make_request"       : ["--make_request"        , "-re"],
    #"make_request"       : ["--make_request"     , "-re"],
    #"run"                : ["--run"              , "-r" ],

    "help"               : ["--help"             , "-h" ],
    #"force_run"          : ["--force_run"        , "-fr"],
    #"migrate"            : ["--migrate"          , "-m" ],
    

_Cascabel actualmente se encuentra bajo desarrollo, esto puede generar que la creación de plantillas de proyectos en futuras versiones no sean compatibles con la actual._
