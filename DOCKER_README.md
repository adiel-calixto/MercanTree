# Requisítos

- [Docker](https://www.docker.com/get-started/)

# Como iniciar

Copie o arquivo de configuração

```bash
    cp mercantree-fe/.env.example mercantree-fe/.env
```

Inicie os containers

```bash
    docker compose up
```

Gere um usuário administrador

```bash
    docker exec -it mercantree-api-1 python manage.py createsuperuser
```
