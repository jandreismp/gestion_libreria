DATAGEDE
========

##### Sistema de Gestión de Integralidad para los Estudiantes Universitarios

## Requisitos Previos

Antes de comenzar, asegúrate de tener los siguientes requisitos:

    * Python 3.12+
    * pip
    * virtualenv (opcional, pero recomendado)
---

## Instalación

   1. Clona el repositorio:
```bash
git clone https://github.com/jandreismp/gestion_libreria.git
cd gestion_libreria
```
2. Crea y activa un entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate  # En Linux usa `source .venv/bin/activate`
```
3. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```
   4. Aplica las migraciones de la base de datos:
```bash
python manage.py migrate
```

## Uso

   1. Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

   2. Para acceder a la web:
<http://127.0.0.1:8000/>
