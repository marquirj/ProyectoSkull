# coding: utf-8

from fabric.api import sudo, cd, env, run, shell_env
import os


def instalacion():
    # Descargamos el repositorio
    sudo('git clone https://github.com/marquirj/ProyectoSkull.git')
    sudo('pip install flask')
    sudo('pip install -r ~/ProyectoSkull/requirements.txt')

def borrar():
    # Borramos directorio repo
    sudo(' rm -rf ./ProyectoSkull')

def levantar():
     # Iniciamos el servicio web
     sudo('nohup python /home/black-wildflower-99/ProyectoSkull/bot/app.py',pty=False)
