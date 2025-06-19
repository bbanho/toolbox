# 🐳 Docker Guidelines

## English

- Keep Dockerfiles and related scripts in the toolbox repository. Do not duplicate them in project repositories.
- Document Docker usage in this file with clear instructions and example commands for building and running containers locally.
- Use multi-stage builds when possible to keep images small and builds fast.
- Map volumes for local development (e.g., `-v $(pwd):/app`).
- Expose only necessary ports (e.g., `-p 8080:80`).
- Keep Docker images generic; use environment variables or build args for customization.
- Test Docker containers in different environments (Linux, macOS, Windows).
- Tag stable Docker configurations and document changes in the changelog.
- Do not store sensitive data in Docker images; use environment variables or secrets management.

### Example: Running a local static server with Docker

```Dockerfile
# Dockerfile
FROM nginx:alpine
COPY . /usr/share/nginx/html
EXPOSE 80
```

Build and run:
```bash
docker build -t pyx-static-site .
docker run -p 8080:80 -v $(pwd):/usr/share/nginx/html pyx-static-site
```

---

## Português

- Mantenha Dockerfiles e scripts relacionados no repositório da toolbox. Não duplique nos repositórios de projetos.
- Documente o uso do Docker neste arquivo, com instruções claras e exemplos de comandos para build e execução local.
- Prefira multi-stage builds para manter as imagens pequenas e o build rápido.
- Mapeie volumes para desenvolvimento local (ex: `-v $(pwd):/app`).
- Exponha apenas as portas necessárias (ex: `-p 8080:80`).
- Mantenha as imagens Docker genéricas; use variáveis de ambiente ou argumentos de build para customização.
- Teste os containers Docker em diferentes ambientes (Linux, macOS, Windows).
- Marque versões estáveis das configurações Docker e documente mudanças no changelog.
- Não armazene dados sensíveis nas imagens Docker; use variáveis de ambiente ou gerenciamento de segredos.

### Exemplo: Servidor estático local com Docker

```Dockerfile
# Dockerfile
FROM nginx:alpine
COPY . /usr/share/nginx/html
EXPOSE 80
```

Build e execução:
```bash
docker build -t pyx-static-site .
docker run -p 8080:80 -v $(pwd):/usr/share/nginx/html pyx-static-site
``` 