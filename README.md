# Introducción a Python para Analistas de Negocio
Este repositorio contiene los materiales (láminas, scripts, ejemplos de código) para el curso de Introducción a Python para Analistas de Negocio.

Estos materiales han sido diseñados considerando:
* Poco conocimiento previo respecto a Python y otros lenguajes de programación.
* Pueden ser usados en modalidad de clase o auto estudio.
* Son prácticos, contienen ejemplos y ejercicios que pueden reproducirse fácilmente.
* Introducen conceptos de forma progresiva.

## Consideraciones del repositorio
Todos los materiales han sido integrados en un repositorio considerando:
* Conjunto de láminas, notebooks y scripts con código compartidas.
* Ambiente GitHub Codespaces para la ejecución de las demostraciones, prácticas y ejercicios.
* Publicación de láminas en un ambiente de hosting Web.
## Dependencias del repositorio
* Instalación de Python versión 3.x
    * Este curso ha sido validado en un ambiente Anaconda con Python 3.8.
* Servidor de Jupyter.
* `node.js` para visualizar los slides de forma local.
## Estructura del repositorio
* topics
    * Directorio con los temas del curso.
* slides
    * Directorio con láminas con código en formato ipynb.
* docs
    * Submódulo de Reveal.js para visualizar las láminas
### Directorio docs 
Para visualizar los slides de forma local es necesario 
* Navegar al directorio `docs`
    * Ejecutar `git submodule init`
    * Ejecutar `git submodule update`
* Navegar al directorio `slides`
    * Ejecutar `build_slides.sh`, el cual copia los archivos slides/*.slides.html a `docs`
* Navegar nuevamente al directorio `docs` y ejecutar
    * `npm install`
    * `npm start`
