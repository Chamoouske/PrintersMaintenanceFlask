<h1 align="center">Control Printers Maintenance</h1>

<div align="center">

### Projeto para controle de manutenção de impressoras
---
![Issues](https://img.shields.io/github/issues/Chamoouske/PrintersMaintenanceFlask)
![Forks](https://img.shields.io/github/forks/Chamoouske/PrintersMaintenanceFlask)
![Stars](https://img.shields.io/github/stars/Chamoouske/PrintersMaintenanceFlask)
![Licence](https://img.shields.io/github/license/Chamoouske/PrintersMaintenanceFlask)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
</div>

- [Features](#features)
- [Demonstração da aplicação](#demonstração-da-aplicação)
- [Pré-requisitos](#pré-requisitos)
- [Rodando a aplicação](#rodando-a-aplicação)
- [Tecnologias](#tecnologias)
- [Autor](#autor)

<div align="center">

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-%233059c1?style=for-the-badge)
</div>

## Features
---
- [x] CRUD Impressoras
- [x] CRUD Manutenções
- [ ] Sistema de login

## Demonstração da aplicação
---
<div style="text-align:justify;">

Tem um exemplo de como a aplicação funciona [aqui](https://control-printers-maintenance.herokuapp.com/), o deploy deste exemplo foi usando a plataforma [Heroku](https://www.heroku.com).
</div>

## Pré-requisitos
---
<div style="text-align:justify;">

Por se tratar de uma aplicação em Flask, será necessário ter instalado na máquina que será o servidor, o [Python](https://www.python.org/) antes de tudo, junto com o [Git](https://git-scm.com), ou apenas baixar o repositório zipado [aqui](https://github.com/Chamoouske/PrintersMaintenanceFlask/archive/refs/heads/main.zip) e seguir os passos descritos após o passo para clonar o repositório.
</div>

## Rodando a aplicação
---
<div style="text-align:justify;">

Caso seja usado um Banco de Dados já criado, altere o caminho expecificado na linha 8 do arquivo [db_manager.py](/src/controller/db_manager.py), seguindo as instruções do [SQLAlchemy](https://docs.sqlalchemy.org/en/14/core/engines.html). Caso contrário, a aplicação criará um arquivo chamado database.db, que armazenará os dados alimentados na aplicação.

Após esses detalhes, seguiremos com os seguintes passos:

```bash
# Clone o repositório
git clone https://github.com/Chamoouske/PrintersMaintenanceFlask.git

# Acesse a pasta do projeto
cd PrintersMaintenanceFlask

# Crie um ambiente virtual antes de prosseguir, siga os passos descritos em <https://docs.python.org/pt-br/3/library/venv.html> para criar
# Instale as depêndencias
pip install -r requeriments.txt

# Execute a aplicação
py app.py

# A aplicação irá rodar na porta 5000 - acesse <http://localhost:5000>
```
</div>

## Tecnologias
---
Este projeto fez uso das seguintes tecnologias:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Gunicorn](https://gunicorn.org/) (Usado apenas para realizar o deply pelo Heroku, pode ser removido do arquivo [requirements.txt](requirements.txt))

## Autor
---
<a href='https://github.com/Chamoouske' target="_blank">
<img src="https://github.com/Chamoouske.png" style="width:100px" />

Ajax Lima
</a>

Feito com ❤️ por Ajax Lima

[![Twitter Badge](https://img.shields.io/badge/-@chamoouske-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/chamoouske)](https://twitter.com/chamoouske)
[![Linkedin Badge](https://img.shields.io/badge/-Ajax%20Lima-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/ajaxlima/)](https://www.linkedin.com/in/ajaxlima/)
[![Gmail Badge](https://img.shields.io/badge/-ajaxlima94@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:ajaxlima94@gmail.com)](mailto:ajaxlima94@gmail.com)

<div align="center">

![Licence](https://img.shields.io/github/license/Chamoouske/PrintersMaintenanceFlask)
</div>