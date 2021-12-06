# Git
Git es un sistema para dar seguimiento a cambios en cualquier conjunto de archivos. Generalmente se usa para coordinar el trabajo entre desarrolladores de software quienes desarrollan código fuente de forma colaborativa. Sus metas incluyen velocidad, integridad de datos, soporte para flujos de trabajo distribuidos no lineales (miles de branches en paralelo corriendo en distintos sistemas).

La interfaz primaria de Git es la línea de comando. Git mantiene una base de datos con estructura no apta para análisis directo por personas. Git mantiene un registro de los cambios realizados a los archivos y provee de comandos para acceder y actualizar el código en la base de datos.

## Beneficios del control de versiones
* Integrar el trabajo de múltiples colaboradores.
* Comprender los cambios.
* Habilitar desarrollo incremental.
* Comparar y revertir cambios a versiones previas.
* Contar con respaldos.
* Contar con múltiples versiones en paralelo.
* Contar con documentación del desarrollo.

## TODO: Configura Git 
Configura Git con tu nombre y dirección de correo por medio de los siguientes estatutos en la línea de comando:
```
$ git config --global user.name "Nombre Apellido"
$ git config --global user.email "email@example.com"
```
# GitHub
GitHub es un proveedor de hosting para desarrollo de software y control de versiones por medio de Git. Ofrece control de versiones distribuidas y administración de código como parte de la funcionalidad clásica de Git, así como sus propias características (issues, pull requests, Codespaces).

## El flujo de GitHub
El flujo de GitHub es ligero, permite experimentar y colaborar en los proyectos fácilmente. Evita el riesgo de perder el trabajo previo.

## Repositorios
Un repositorio es el recurso donde se lleva a cabo el trabajo del proyecto el cual podemos relacionar con una carpeta de proyecto. Contiene todos los archivos de proyecto e historial de revisiones. Es posible trabajar con un repositorio de forma autónoma o invitar a otras personas a colaborar.

## Clonado
Cuando un repositorio se crea en GitHub, se almacena de forma remota en la nube. Es posible clonar un repositorio para crear una copia local en la computadora y usar Git para sincronizar ambos. Esto facilita corregir problemas, añadir, modificar o eliminar archivos y empujar commits grandes. 

Es posible usar herramientas de edición de código, en vez de la interfaz Web de GitHub, para realizar los cambios al código del repositorio. Cuando se clona un repositorio, se descargan todos los datos del repositorio que GitHub tiene hasta ese momento en el tiempo, incluyendo todas las versiones de todos los archivos y carpetas en el proyecto. Esto puede ser útil para experimentar con el proyecto.

## Commit y push
Commit y push son los medios para añadir cambios realizados en la computadora local al repositorio remoto en GitHub. De esta forma tu facilitador o compañeros podrán ver tu trabajo más reciente cuando estés listo para compartirlo. Es posible hacer un commit cuando hayas efectuado cambios al proyecto que quieres resguardar. También es posible añadir un mensaje al commit para recordar el trabajo realizado con ese cambio.

Tan pronto tengas uno o múltiples commits que estés listo para publicar, es posible usar el comando push para añadir esos cambios al repositorio remoto. Después de un tiempo te resultará familiar efectuar los procesos de commit y push.

## Repositorios: Más detalles
Es muy probable que con el tiempo crees múltiples repositorios en GitHub, por medio del *GitHub Dashboard* es posible navegar entre todos los repositorios y ver información útil acerca de ellos.

Los repositorios contienen archivos README. Estos archivos pueden ser empleados para describir el proyecto a otras personas, por qué es útil, qué pueden hacer con él y cómo pueden usarlo. 

## Branches
Es posible emplear branches en GitHub para aislar trabajo que no quieras integrar a tu proyecto final aún. Los branches permiten implementar nuevas características, corregir errores, experimentar de forma segura con una idea nueva en un área independiente del repositorio. Típicamente podrías crear un nuevo branch a partir del branch default del repositorio que se llama **main** por omisión. Esto crea una nueva copia de trabajo del repositorio para experimentar. Es posible unir los cambios realizados en un branch al branch **main**.

## Forks
Un fork es otra forma de copiar un repositorio, generalmente empleado para contribuir a un proyecto de alguien más. Un repositorio creado por medio de fork permite experimentar de forma libre con cambios sin afectar el proyecto original y es muy popular entre quienes contribuyen a proyectos de código abierto.

## Pull Requests
Es posible emplear un Pull Request para informar a otros acerca de cambios que se desean integrar a un branch y solicitar su retroalimentación. Cuando se abre un pull request, es posible revisar y discutir los cambios potenciales con colaboradores y añadir más cambios en caso de ser necesario. Es posible añadir a personas específicas como revisores de un pull request lo cual indica que deseas su retroalimentación de tus cambios. Cuando un pull request está listo, es posible integrarlo en el branch de interés (**main**, generalmente).

## Issues
Los issues son un medio para dar seguimiento a mejoras, tareas o errores asociados con tu trabajo en GitHub. Los issues son una excelente forma de dar seguimiento a todas las tareas en las que quieres trabajar para tu proyecto, así como informar a otros respecto a tus planes. También es posible usar issues para informar a proyectos open source de terceros respecto a un bug o una solicitud.

En el caso de proyectos grandes, es posible dar seguimiento a los issues por medio de un board del proyecto. GitHub Projects ayuda a organizar y priorizar el trabajo. También permiten asociar pull requests e issues para mostrar que una corrección se encuentra en proceso y cerrar automáticamente el issue cuando de integre (merge) el pull request.

# GitHub Codespaces
GitHub Codespaces es un ambiente de desarrollo que reside en la nube. Es posible personalizar proyectos para Codespaces al integrar archivos de configuración al repositorio, soportando la noción de Configuration-As-Code. GitHub Codespaces provee de una configuración repetible del codespace para todos los usuarios del proyecto.

Es posible acceder un codespace desde Visual Studio Code o desde un navegador de Internet por medio del cual se tendrá acceso al editor de código, depurador, control de versiones, sincronización de parámetros de configuración y todo el ecosistema de extensiones

Codespaces provee de imágenes para proyectos de cualquier tamaño y soporta conexiones de baja latencia entre las cuatro regiones donde está desplegado el servicio.

Codespaces provee de devcontainer.json como un medio de estandarización para el entorno, tiempo de ejecución, especificaciones de hardware, extensiones y configuración del editor, facilitando la inducción a nuevos integrantes al equipo de trabajo. Es posible aislar dependencias entre proyectos por medio de contenedores y docker-compose.

Codespaces soporta previsualización de aplicaciones instantáneas en un navegador (con websockets y HMR), así como compartir puertos privados y públicos entre miembros del equipo de trabajo.

# Visual Studio Code
Visual Studio Code es un editor de código fuente desarrollado por Microsoft, disponible para Windows, Linux y MacOS. Cuenta con soporte para depuración, coloración de sintaxis, completado de código, refactoring de código y soporte a Git integrado. Es personalizable y extensible.

## Interfaz de usuario
Visual Studio Code cuenta con un explorador integrado de archivos
* **Editor**: El área principal donde se editan los archivos. Es posible abrir múltiples editores de forma vertical u horizontal.
* **Barra lateral**: Contiene la vista del explorador, entre otras, para brindar asistencia mientras se trabaja en el proyecto.
* **Barra de estatus**: Con información del proyecto abierto y los archivos que se están editando.
* **Barra de actividades**: Permite cambiar entre vistas y otorga indicaciones adicionales de contexto como el número de cambios pendientes en Git.
* **Páneles**: Proveen información de salidas de consola, depuración, errores, advertencias. La terminal integrada también se encuentra en esta región.

## Archivos
Visual Studio Code cuenta con un editor de archivos con soporte a coloración de sintaxis para múltiples lenguajes de programación.

## Paleta de comandos
Visual Studio Code es accesible por medio del teclado. La combinación de teclas `Ctrl+Shift+P` abre la paleta de comandos. Desde la paleta de comandos es posible acceder a toda la funcionalidad de Visual Studio Code, también muestra los atajos de teclado para operaciones frecuentes.

## Extensiones
Las extensiones de Visual Studio Code son un mecanismo para añadir lenguajes depuradores y herramientas a la instalación para dar soporte a tu flujo de trabajo de desarrollo. Las extensiones se encuentran publicadas en el Visual Studio Code Marketplace.

## Terminal Integrada
Visual Studio Code cuenta con una terminal integrada completamente funcional que inicia en el directorio raíz del espacio de trabajo. Cuenta con integración con el editor para dar soporte a características como links y detección de errores.

La terminal integrada puede usar diversos shells instalados en la computadora. Por omisión:
* PowerShell en Windows.
* bash en macOS y Linux.

Nota: Shell es un programa que procesa comandos y regresa una salida. Una terminal es un programa que ejecuta un shell.

## Notebooks Jupyter
Jupyter es un proyecto open source que permite combinar texto Markdown y código fuente ejecutable Python en un canvas llamado notebook. Visual Studio Code soporta trabajar con Jupyter Notebooks de forma nativa y por medio de archivos de código Python.

Por medio de Jupyter Notebooks en Visual Studio Code es posible:
* Crear, abrir y guardar Jupyter Notebooks.
* Trabajar con celdas de código de Jupyter.
* Visualizar, inspeccionar y filtrar variables usando Variable Explorer y Data Viewer.
* Conectar a un servidor remoto Jupyter.
* Depurar un Jupyter Notebook.

Notas:
* Para trabajar con Python en Jupyter Notebook se requiere activa un ambiente Anaconda en Visual Studio Code o en otro ambiente Python en el que se haya instalado el paquete Jupyter. Es posible seleccionar un ambiente por medio del comando Python: **Select Interpreter** en la paleta de comandos.






