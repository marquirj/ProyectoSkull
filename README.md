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

# Despliegue Docker

Primero instalo Docker en Ubuntu 16.04 LTS, para ello sigo los pasos que se [indica.](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#upgrade-docker-after-using-the-convenience-script)

Luego ejecuto el servicio con el comando: sudo service docker start
 ![Start](/img/6.png)

 Una vez creado, me registro en Docker y enlazo con mi repositorio de github.

 ![Registro](/img/8.png)

 Ahora enlazo y creo en Docker.

 ![Enlazado](/img/7.png)

Y una vez añadido el Dockerfile, vemos que compila.

![Construcción](/img/9.png)

[Enlace a Docker](https://hub.docker.com/r/marquirj0/proyectoskull/)


# Despliegue en Zeit

Para le despliegue en Zeit es necesario instalar now, primero he instalado nvm, y una vez instalado descargo now con la orden npm install -g now.

En la carpeta de nuestro proyecto ejecuto: now --public y listo.

Contenedor: https://proyectoskull-isnentwdjf.now.sh
