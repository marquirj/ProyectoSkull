# coding: utf-8

from fabric.api import sudo, cd, env, run, shell_env
import os
def instalacion():
    sudo('git clone https://github.com/marquirj/ProyectoSkull.git')
    sudo('pip install flask')
    sudo('pip install -r ~/ProyectoSkull/requirements.txt')
def borrar():
    sudo(' rm -rf ./ProyectoSkull')
def levantar():
     sudo('nohup python /home/black-wildflower-99/ProyectoSkull/bot/app.py',pty=False)
