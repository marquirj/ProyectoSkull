[![Build Status](https://travis-ci.org/marquirj/ProyectoSkull.svg?branch=master)](https://travis-ci.org/marquirj/ProyectoSkull)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=hhttps://github.com/marquirj/ProyectoSkull)

# Proyecto Skull

 1. Este proyecto consiste en la creación de un servicio de sincronización de resultados. En primer momento pensé en hacer la aplacación de resultados de la primera división española, pero debido al nombre he pensado que podía crear el servicio para la liga andaluza de Cádiz, donde milita el equipo de mi pueblo.
 2. El lenguaje de programación que se usaré será Python.
 3. Mi intención era montar una base de datos MySql, pero una vez usado Heroku y viendo que incorpora un addon para PostgreSQl, usaré esa base de datos.

## Integración Continua.

 Usaré TDD para ir haciendo pruebas para desarrollar el proyecto. 

# Despliegue Heroku.

Me registro en el servicio PaaS, Heroku.

![Imagen darse de alta](/img/1.png)

Verificando que accedo dentro de la aplicación con un usuario.

![Comprobación](/img/2.png)

Creo una aplicación en Heroku, estos mismos pasos serán seguidos para la creación de mi aplicación, ProyectoSkull.

![Crear Proyecto prueba](/img/3.png)

Un ejemplo comprobar los logs de la aplicación.

![Logs](/img/4.png)


Enlazo la aplicación con GitHub.

![Enlazado](/img/5.png)

Indico el despliegue:

Despliegue https://proyectoskullapp.herokuapp.com/
