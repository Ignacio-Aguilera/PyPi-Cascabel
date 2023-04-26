
from genericpath import isfile
import os, sys, shutil, colorama
from urllib import request
cmd_dir  = os.getcwd()
file_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/").replace("/classes", "")

class Cascabel:
    
    VERSION = "LOCAL_TEST"
    #================================================================================================
    
    def print_simplify_logo (self):

        w_c = colorama.Style.RESET_ALL
        y_c = colorama.Fore.YELLOW

        logo =   y_c + "   _______  _\n"
        logo +=  y_c + "  /  __  c\\|_|\n"
        logo +=  y_c + " |  /  \__/|__|\n"
        logo +=  y_c + " |  |      | __|\n"
        logo +=  y_c + " |  \__/\\  | |\n"
        logo +=  y_c + "  \_____/ |_/  versión " + self.VERSION + "\n" + w_c

        print(logo)
        

    def print_logo (self):

        clear_command = 'cls' if os.name in ('nt', 'dos') else 'clear'
        os.system(clear_command)

        w_c = colorama.Style.RESET_ALL #Si la consola es oscura se muestra de color blanco y viceversa.
        y_c = colorama.Fore.YELLOW

        logo =   f"{y_c}   _______  {w_c}                       _            {y_c} _\n"
        logo +=  f"{y_c}  /  __  c\\{w_c}                       | |          {y_c} |_|\n"
        logo +=  f"{y_c} |  /  \__/{w_c}__ _  ___   ___   __ _ | |__    ___  {y_c}|__|\n"
        logo +=  f"{y_c} |  |     {w_c}/ _' |/ __| / __| / _' || '_ \  / _ \\{y_c} | __|\n"
        logo +=  f"{y_c} |  \__/\\{w_c}| (_| |\__ \| (__ | (_| || |_) ||  __/{y_c} | |\n"
        logo +=  f"{y_c}  \_____/ {w_c}\__,_||___/ \___| \__,_||_.__/  \___|{y_c}|_/  versión {self.VERSION} \n {w_c}"

        print(logo)

        import platform
        
        if os.path.isfile(f"{os.getcwd()}/routes.py") and os.path.isfile(f"{os.getcwd()}/config.py") and os.path.isfile(f"{os.getcwd()}/execute.py"):
            is_project_dir = "Si"
        else:
            is_project_dir = "No"
            
    
        print(' Sistema Operativo:', platform.system() )
        print(' Platafotma       :', sys.platform)
        print(' Distribucion     :', platform.platform())
        print(' Version de python:', sys.version.replace('\n',''))
        print(' Version dict     :', sys.version_info)
        print(' Ejecutable actual:', sys.executable)
        print(' Argumentos       :', sys.argv)
        print(' Ruta actual      :', os.getcwd())
        print(' Ruta de projecto?:', is_project_dir)
        print(' Ruta de ejecución:', os.path.dirname(os.path.realpath(__file__)))
        print('')

    def catch_error(self):

        w_c = colorama.Fore.WHITE
        y_c = colorama.Fore.YELLOW

        Cascabel().print_logo()

        from cascabel.dictionaries.commands import commands, full_commands
        
        print(" Comando no valido")

        import difflib
        import itertools

        keys = list(commands.keys())
        values = list(itertools.chain.from_iterable(commands.values()))

        all_words = keys + values

        coincidences = difflib.get_close_matches(sys.argv[1], all_words)

        if len(coincidences) != 0:

            coincidence = coincidences[0]

            if coincidence in keys:
                possible_command = full_commands[coincidence]
            else:
                for key, value in commands.items():
                    if coincidence in value:
                        possible_command = full_commands[key]
                        break
                    
            print(f"\n ¿Quisiste ejecutar el siguiente comando '{y_c}{possible_command}{w_c}' ?")

    def verify_libraries(self):
        self.print_logo()

        w_c = colorama.Style.RESET_ALL
        y_c = colorama.Fore.YELLOW
        r_c = colorama.Fore.RED

        print(y_c + " Librerias Necesarias" + w_c)

        try:
            import flask
            print(" |- Flask  : Instalado")
        except:
            print(" |- Flask  : " + r_c + "No instalado" + w_c)

        try:
            import dotenv 
            print(" |- Dotevn: Instalado")
        except:
            print(" |- Dotevn: " + r_c + "No instalado" + w_c)

        try:
            import flask_wtf
            print(" |- Flask-WTF: Instalado")
        except:
            print(" |- Flask-WTF: " + r_c + "No instalado" + w_c)

        try:
            import flask_sqlalchemy 
            print(" |- Flask-SqlAlchemy: Instalado")
        except:
            print(" |- Flask-SqlAlchemy: " + r_c + "No instalado" + w_c) 


        print("\n Puedes instalar las librerias manualmente o utilizando " + y_c + "'--install_libraries'" + w_c)

    def install_libraries(self):

        import platform
        
        w_c = colorama.Style.RESET_ALL #Si la consola es oscura se muestra de color blanco y viceversa.
        y_c = colorama.Fore.YELLOW

        executable = sys.executable

        self.print_logo()

        if (sys.version).find('3.') > -1:
            
            try:
                import pip

                try:
                    import flask
                    return_code_1 = '0'
                except:
                    self.print_logo()
                    return_code_1 = os.system(f"{executable} -m pip install Flask")
                    
                try:
                    import dotenv
                    return_code_2 = '0' 
                except:
                    self.print_logo()
                    return_code_2 = os.system(f"{executable} -m pip install python-dotenv")

                try:
                    import flask_wtf
                    return_code_3 = 0
                except:
                    self.print_logo()
                    return_code_3 = os.system(f"{executable} -m pip install Flask-WTF")

                try:
                    import flask_sqlalchemy
                    return_code_4 = 0
                except:
                    self.print_logo()
                    return_code_4 = os.system(f"{executable} -m pip install flask-sqlalchemy")

                #self.print_logo()
                print(" flask:", return_code_1)    
                print(" dot_env:", return_code_2)
                print(" flask_wtf:", return_code_3)
                print(" flask_sqlalchemy:", return_code_4)

            except: 
                print(" Se detuvo la instalación debido a que no se detecto pip")
            
        else:
            print(" Esta función solo esta disponible para python 3")

       
    def show_info(self):

        self.print_logo()

        print(" Versión de python : " + sys.version.split(" ")[0] + "\n")
        print(" Desarrollado por Ignacio Aguilera")

    def show_help(self):
        self.print_logo()

        from cascabel.dictionaries.commands import full_commands
    
        for key, command in full_commands.items():
            print(f' {key.ljust(20)} -> {command}')

    def create_new_project(self):

        project_name = sys.argv[2].lower()
        project_dir  = f'{cmd_dir}/{project_name}/'
        template_dir = f'{file_dir}/data/template/project/'

        if os.path.isdir((project_dir)):
            self.print_logo()
            print(f" Ya existe una carpeta con el nombre '{project_name}' en el directorio actual")
        else:
            self.print_logo()
            shutil.copytree(template_dir, project_dir, ignore=None)
            print(" La plantilla del proyecto ha sido creada correctamente")
    
    def make_controller(self):

        self.print_logo()

        controller_name = sys.argv[2].lower()
        controller_class_name = controller_name.replace("_", " ").title().replace(" ", "") + "Controller"

        project_dir  = f'{cmd_dir}/'
        controller_template_dir = f'{file_dir}/data/template/controller/simple_controller.py'

        content = open(controller_template_dir, "r").read().replace("NAME", controller_class_name)
        
        if os.path.isdir(project_dir + "app/controllers/") and os.path.isfile(project_dir + "routes.py"):
            if not os.path.isfile(project_dir + "app/controllers/" + controller_name +"_controller.py"):
                file = open(project_dir + "app/controllers/" + controller_name + "_controller.py", "w")
                file.write(content)
                file.close()

                routes_content = open(project_dir + "routes.py", "r+").read()
                import_stat = f"\nfrom app.controllers.{controller_name}_controller import {controller_class_name}\n"
                import_route_stat = "from resources.routes.route import Route\n"
                add_route_stat = f"Route().add_route(app, 'GET', '/{controller_name}',  {controller_class_name}().index , '{controller_name}_index') \n"
                

                if routes_content.count(import_route_stat) == 0:
                    routes_content = import_route_stat + routes_content +  import_stat + add_route_stat
                    
                else:
                    routes_content = routes_content +import_stat + add_route_stat
                
                file = open(project_dir + "routes.py", "w").write(routes_content)

                print(" El controlador sido creada correctamente")
            else:
                print(" Error el archivo ya existe")
        else:
            print(" Directorio invalido")

    def make_request(self):
        
        self.print_logo()

        request_name = sys.argv[2].lower()
        request_class_name = request_name.replace("_", " "). title().replace(" ", "") + "Request"

        project_dir  = f'{cmd_dir}/'
        request_template_dir = f'{file_dir}/data/template/request/request.py'

        content = open(request_template_dir, "r").read().replace("NAME", request_class_name)

        if not os.path.isdir(project_dir + "app/requests/") or not os.path.isfile(project_dir + "routes.py"):
            print(" Directorio invalido")
            return None

        if os.path.isfile(project_dir + "app/requests/" + request_name +"_controller.py"):
            print(" Error el archivo ya existe")
            return None

        file = open( f"{project_dir}app/requests/{request_name}_request.py", "w")
        
        file.write(content)
        file.close()

    def make_manager_controller(self):

        self.print_logo()

        controller_name = sys.argv[2].lower()
        controller_class_name = controller_name.replace("_", " ").title().replace(" ", "") + "Controller"

        project_dir  = f'{cmd_dir}/'
        controller_template_dir = f'{file_dir}/data/template/controller/manager_controller.py'

        content = open(controller_template_dir, "r").read().replace("CLASSNAME", controller_class_name).replace("NAME", controller_name)
        
        if not os.path.isdir(project_dir + "app/controllers/") or not os.path.isfile(project_dir + "routes.py"):
            print(" Directorio invalido")
            return None
        
        if os.path.isfile(project_dir + "app/controllers/" + controller_name +"_controller.py"):
            print(" Error el archivo ya existe")
            return None
        
        file = open(project_dir + "app/controllers/" + controller_name + "_controller.py", "w")
        file.write(content)
        file.close()

        routes_content = open(project_dir + "routes.py", "r+").read()
        import_stat = f"\nfrom app.controllers.{controller_name}_controller import {controller_class_name}\n"
        import_route_stat = "from resources.routes.route import Route\n"
        add_route_stat =  f"Route().add_route(app, 'GET', '/{controller_name}',  {controller_class_name}().index , '{controller_name}_index') \n"
        add_route_stat += f"Route().add_route(app, 'GET', '/{controller_name}/view/<id>',  {controller_class_name}().view , '{controller_name}_view') \n"
        add_route_stat += f"Route().add_route(app, 'GET', '/{controller_name}/store',  {controller_class_name}().get_store , 'get_{controller_name}_store') \n"
        add_route_stat += f"Route().add_route(app, 'POST', '/{controller_name}/store',  {controller_class_name}().post_store , 'post_{controller_name}_store') \n"
        add_route_stat += f"Route().add_route(app, 'GET', '/{controller_name}/update/<id>',  {controller_class_name}().get_update , 'get_{controller_name}_update') \n"
        add_route_stat += f"Route().add_route(app, 'POST', '/{controller_name}/update/<id>',  {controller_class_name}().post_update , 'post_{controller_name}_update') \n"
        add_route_stat += f"Route().add_route(app, 'POST', '/{controller_name}/delete/<id>',  {controller_class_name}().delete , '{controller_name}_delete') \n"

        if routes_content.count(import_route_stat) == 0:
            routes_content = import_route_stat + routes_content +  import_stat + add_route_stat
        else:
            routes_content = routes_content +import_stat + add_route_stat
        
        file = open(project_dir + "routes.py", "w").write(routes_content)

        controller_html_path = f'templates/{controller_name}' 
        if not os.path.exists(controller_html_path):
            os.makedirs(controller_html_path)

        html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PAGE</title>
</head>
<body>
    <p>PAGE</p>
</body>
</html>
        """

        file = open(controller_html_path + "/index.html", "w").write(html_content.replace('PAGE', f'{controller_name}_index'))
        file = open(controller_html_path + "/view.html", "w").write(html_content.replace('PAGE', f'{controller_name}_view'))
        file = open(controller_html_path + "/store.html", "w").write(html_content.replace('PAGE', f'get_{controller_name}_store'))
        file = open(controller_html_path + "/update.html", "w").write(html_content.replace('PAGE', f'get_{controller_name}_update'))

        print(" El controlador sido creada correctamente")
    
    def make_model(self):
        self.print_logo()

        model_name = sys.argv[2].lower()
        model_bind = sys.argv[3]
        model_class_name = model_name.replace("_", " ").title().replace(" ", "") + "Model"

        project_dir  = f'{cmd_dir}/'
        model_template_dir = f'{file_dir}/data/template/model/model.py'

        content = open(model_template_dir, "r").read()
        content = content.replace("TABLE_NAME", model_name)
        content = content.replace("NAME", model_class_name)
        content = content.replace("BIND", model_bind)
        

        if not os.path.isdir(project_dir + "app/models/") or not os.path.isfile(project_dir + "routes.py"):
            print(" Directorio invalido")
            return None
        
        if os.path.isfile(project_dir + "app/models/" + model_name +"_model.py"):
            print(" Error el archivo ya existe")
            return None
        
        file = open(project_dir + "app/models/" + model_name + "_model.py", "w")
        file.write(content)
        file.close()

        database_content = open(project_dir + "database_config.py", "r+").read()
        import_stat = f"from app.models.{model_name}_model import {model_class_name}\n"

        database_content =  database_content + import_stat
 
        file = open(project_dir + "database_config.py", "w").write(database_content)

        print(" El controlador sido creada correctamente")
