#!/bin/bash
echo "Instalando venv"
sudo apt install python3.10-venv
echo "Criando ambiente"
python3 -m venv env_py
echo "Conectando ao ambiente"
source env_py/bin/activate
echo "Instalando bibliotecas"
pip3 install python-dotenv pyexcel pyexcel-ods jinja2

