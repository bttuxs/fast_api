# Fast API

## _Creacion de API base con Fast API_

[![N|Solid](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com)

Se crea proyecto base de Fast API con una arquitectura modular y con el uso de conexion con postgresql

## Requerimientos

- [Python](https://www.python.org/downloads/) version 3.9.6
- [PyEnv](https://github.com/pyenv/pyenv#installation)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker compose](https://docs.docker.com/compose/install/)

## Ambiente

Instalar dependencias e iniciar el servidor

```sh
pip install -r requeriments.txt
```

## Iniciar el servidor

Teniendo instalado docker y docker comppose en la raiz del proyecto ejecutamos el siguiente comando para levantar la base de datos

```sh
docker compose up --build
```

una vez iniciada la base de datos prodedemos a levantar el aplicativo

```sh
python server.py
```

si el servidor esta corriendo correctamente podriamos ver
acceder a la siguiente url

### [http://localhost:8432/docs](http://localhost:8432/docs)
