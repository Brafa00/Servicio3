# Taller JBS Servicio 3

Este es un codigo de ejemplo para realizar implementaciones de aseguramiento de calidad en el codigo

## Description

Este es un codigo de ejemplo para realizar un codigo en python con FAST API,en el cual se implementara todo los visto en clase:
Servicio REST API funcional y sus respectivos pipelines CD Y CI con integracion de Heroku ,sonar cloud y Slack notifications. 


## Getting Started

### Dependencies

python3

fastapi

uvicorn

requests

pytest

pytest-cov

aioprometheus

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders
Para instalar el proyectos desde cmd daremos el comando :
```
git clone "repo url".
```
Luego de esto ejecutaremos el comando 
```
python3 -m venv .venv   //isolate libraries for this application
```
Luego se debe activa el path 

Para Windows: 
```
\path\to\env\Scripts\activate  //activate virtual env

C:\Users\computer_username\venv\Scripts\activate.bat //Example
```
para So tipo Unix:
```
source .venv/bin/activate  //activate virtual env
```
Luego de esto ejecutaremos el comando:
```
pip install -r requirements.txt
```

### Executing program

Como ejecutar localmente

* Para ejecutar el programa por cmd con el .venv activo escribimso el comando:

```
uvicorn main:app --reload
```

Viste http://localhost:8000/ para ver la aplicacion

Viste http://localhost:8000/metrics para ver las metricas

Viste http://localhost:8000/roleUsers para ver la Api funcional

Para ver los logs de las aplicacion debes instalar Heroku Cli y  ejecutar los sigueintes comandos

```
heroku login
heroku logs --tail -a servicio2
```

*Para ejecutar las pruebas unitarias con covertura:
```
pytest 
```

*Para ejecutar las pruebas unitarias con covertura:
```
pytest -v -o junit_family=xunit1 --cov=. --cov-report=html:src/reports/html_dir --cov-report xml:src/reports/coverage.xml --junitxml=src/reports/nosetests.xml
```
## Help

En caso de tener alguno problema reportarlo a los siguientes mails:
```
-jorge-620@hotmail.com

-brafa02@gmail.com

-sebastian17mm@gmail.com
```



## Authors


ex.Jorge Andrés Garcia Zapata (jorge-620@hotmail.com)

ex.Brayan Rafael Florez Florez (brafa02@gmail.com)

ex. Sebastian Montoya Madrid (sebastian17mm@gmail.com)



## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the GPL License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
* [guia de fast api]https://metal-bard-756.notion.site/Wiki-GreenHouse-3b62c2e91ce64666bc3989025f6078a4
