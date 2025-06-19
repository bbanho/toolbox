# Development Toolbox

> A collection of scripts, utilities, and automations for static web projects and DevOps.

## 📑 Documentation Index

- [Changelog](CHANGELOG.md) - History of changes and versions
- [Contributing Guidelines](CONTRIBUTING.md) - How to contribute to this project
- [Docker Setup](DOCKER.md) - Docker configuration and usage
- [License](LICENSE) - Project license and terms

---

## 📑 Project Guidelines

### English
- Keep all scripts, utilities, and automations in the toolbox repository. Do not duplicate them in project repositories.
- Document every new script or significant change with clear docstrings and README updates.
- Use clear, conventional commit messages (e.g., `feat:`, `fix:`, `docs:`).
- Always create a new branch for features or fixes. Merge only after review and testing.
- Tag stable releases and keep a changelog of important changes.
- Test scripts in different environments before release.
- Reference the toolbox in all projects that use it, and keep it updated via `git pull`.
- Do not include sensitive or project-specific data in the toolbox.
- Prefer English for documentation and comments, but keep Portuguese as a secondary option for accessibility.

### Português
- Mantenha todos os scripts, utilitários e automações no repositório da toolbox. Não duplique nos repositórios de projetos.
- Documente todo novo script ou alteração relevante com docstrings claras e atualização do README.
- Use mensagens de commit claras e padronizadas (ex: `feat:`, `fix:`, `docs:`).
- Sempre crie uma branch para novas features ou correções. Faça merge apenas após revisão e testes.
- Marque releases estáveis com tags e mantenha um changelog das mudanças importantes.
- Teste os scripts em diferentes ambientes antes de liberar.
- Referencie a toolbox em todos os projetos que a utilizam e mantenha-a atualizada com `git pull`.
- Não inclua dados sensíveis ou específicos de um projeto na toolbox.
- Prefira inglês para documentação e comentários, mas mantenha o português como opção secundária para acessibilidade.

## 📚 Features

- **local_server.py**  
  Local HTTP server for static site development.
- **optimize_images.py**  
  Image optimization for the web (JPEG, PNG, WebP).
- **validate_web.py**  
  HTML, accessibility, and performance validation for web pages.
- **gh_commands.sh**  
  Utility commands for GitHub integration (PR, deploy, etc).

## ⚠️ Important Notices

### Initialization Changes
The way projects are initialized and run may change frequently. This is expected and part of our continuous improvement process.

### Known Issues & Solutions

1. **Server Initialization**
   - Different Python versions may require different server commands
   - Some systems might need `python` instead of `python3`
   - Port conflicts are common - try different ports if the default is busy

2. **Image Processing**
   - PPM files are automatically converted to JPG
   - Large images may take longer to process
   - Memory errors might occur with extremely large batches

3. **Validation Tools**
   - Some validations require external services
   - Network issues may affect validation results
   - Cached results might not reflect recent changes

### Quick Fixes
- Clear browser cache frequently
- Keep Python dependencies updated
- Check system requirements before running scripts
- Use `--help` flag for updated command options

## 🚀 Usage

> ⚠️ This toolbox is intended for use by technical users familiar with command-line interfaces, Python environments, and web project structures. 
> The instructions below are intentionally generic and may require adaptation to your specific project architecture. 
> If you are not comfortable with these tools, seek assistance from a developer or system administrator.

Clone the toolbox on your machine:

```bash
# Clone the toolbox repository (replace with your own source control URL)
git clone <toolbox-repository-url>
cd toolbox
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Usage examples

Run local server:
```bash
python local_server.py -p <port> -d <directory>
```

Optimize images:
```bash
python optimize_images.py <image-directory> -q 85 -w 1920
```

Validate site:
```bash
python validate_web.py -u <site-url> -p <path>
```

GitHub commands:
```bash
./gh_commands.sh create-pr "Title" "Description"
```

> **Note:** These scripts are designed to be flexible and require adaptation to your project's structure. They do not provide out-of-the-box solutions for non-technical users.

## 🗂️ Versioning

- **Commits:**  
  Use clear and standardized messages, e.g.:  
  `feat: add accessibility validation to validate_web.py`  
  `fix: fix bug in image optimizer`
- **Branches:**  
  Use branches for new features or fixes.  
  E.g.: `feature/new-script`, `fix/validation-adjustment`
- **Tags/Releases:**  
  Create tags for stable versions:  
  `git tag v1.0.0 && git push origin v1.0.0`
- **Changelog:**  
  Keep a summary of changes in the README or in `CHANGELOG.md`.

## 📝 Best practices

- Scripts should be portable and accept command-line arguments.
- Always document new functions/utilities.
- Do not include sensitive data or project-specific information.
- Update the README with every new feature or relevant change.
- Test scripts in different environments before tagging a release.

## 📦 Integration with other projects

- Do not copy scripts to other repositories.  
  Always use the toolbox as the single source of truth.
- Reference the toolbox in the README of projects that use it.
- To update, simply run `git pull` in the toolbox directory.

## 📄 License

MIT License

---

# Central de Desenvolvimento (Português)

> Central de scripts, utilitários e automações para projetos web estáticos e DevOps.

## 📑 Índice da Documentação

- [Registro de Mudanças](CHANGELOG.md) - Histórico de alterações e versões
- [Guia de Contribuição](CONTRIBUTING.md) - Como contribuir com o projeto
- [Configuração Docker](DOCKER.md) - Configuração e uso do Docker
- [Licença](LICENSE) - Licença e termos do projeto

## 📚 Funcionalidades

- **local_server.py**  
  Servidor HTTP local para desenvolvimento de sites estáticos.
- **optimize_images.py**  
  Otimização de imagens para web (JPEG, PNG, WebP).
- **validate_web.py**  
  Validação de HTML, acessibilidade e performance de páginas.
- **gh_commands.sh**  
  Comandos utilitários para integração com GitHub (PR, deploy, etc).

## ⚠️ Avisos Importantes

### Mudanças na Inicialização
A forma como os projetos são inicializados e executados pode mudar frequentemente. Isso é esperado e faz parte do nosso processo de melhoria contínua.

### Problemas Conhecidos & Soluções

1. **Inicialização do Servidor**
   - Diferentes versões do Python podem exigir comandos diferentes
   - Alguns sistemas podem precisar usar `python` em vez de `python3`
   - Conflitos de porta são comuns - tente portas diferentes se a padrão estiver ocupada

2. **Processamento de Imagens**
   - Arquivos PPM são automaticamente convertidos para JPG
   - Imagens grandes podem demorar mais para processar
   - Erros de memória podem ocorrer com lotes muito grandes

3. **Ferramentas de Validação**
   - Algumas validações requerem serviços externos
   - Problemas de rede podem afetar resultados da validação
   - Resultados em cache podem não refletir mudanças recentes

### Soluções Rápidas
- Limpe o cache do navegador frequentemente
- Mantenha as dependências Python atualizadas
- Verifique os requisitos do sistema antes de executar scripts
- Use a flag `--help` para ver opções de comando atualizadas

## 🚀 Como usar

> ⚠️ Esta toolbox é destinada a usuários técnicos familiarizados com linha de comando, ambientes Python e estruturas de projetos web. 
> As instruções abaixo são propositalmente genéricas e podem exigir adaptação à arquitetura do seu projeto. 
> Se não estiver confortável com essas ferramentas, procure auxílio de um desenvolvedor ou administrador de sistemas.

Clone a toolbox em sua máquina:

```bash
# Clone o repositório da toolbox (substitua pela URL do seu controle de versão)
git clone <url-do-repositorio-da-toolbox>
cd toolbox
```

Instale as dependências Python:

```bash
pip install -r requirements.txt
```

### Exemplos de uso

Rodar servidor local:
```bash
python local_server.py -p <porta> -d <diretório>
```

Otimizar imagens:
```bash
python optimize_images.py <diretorio-de-imagens> -q 85 -w 1920
```

Validar site:
```bash
python validate_web.py -u <url-do-site> -p <caminho>
```

Comandos GitHub:
```bash
./gh_commands.sh create-pr "Título" "Descrição"
```

> **Nota:** Estes scripts são flexíveis e exigem adaptação à estrutura do seu projeto. Não fornecem soluções prontas para usuários não técnicos.

## 🗂️ Versionamento

- **Commits:**  
  Use mensagens claras e padronizadas, ex:  
  `feat: adiciona validação de acessibilidade ao validate_web.py`  
  `fix: corrige bug no otimizador de imagens`
- **Branches:**  
  Use branches para novas features ou correções.  
  Ex: `feature/novo-script`, `fix/ajuste-validacao`
- **Tags/Releases:**  
  Crie tags para versões estáveis:  
  `git tag v1.0.0 && git push origin v1.0.0`
- **Changelog:**  
  Mantenha um resumo das mudanças no README ou em `CHANGELOG.md`.

## 📝 Boas práticas

- Scripts devem ser portáveis e aceitar argumentos de linha de comando.
- Sempre documente novas funções/utilitários.
- Não inclua dados sensíveis ou específicos de um projeto.
- Atualize o README a cada nova funcionalidade ou mudança relevante.
- Teste scripts em diferentes ambientes antes de marcar uma release.

## 📦 Integração com outros projetos

- Não copie scripts para outros repositórios.  
  Sempre utilize a toolbox como fonte única.
- Referencie a toolbox no README dos projetos que a utilizam.
- Para atualizar, basta dar `git pull` na toolbox.

## 📄 Licença

MIT License

---

## 🌐 Static Pages Repository

> 🗂️ **All static site files (HTML, CSS, images, JSON) are maintained in the [pyx-engenharia-portfolio](../pyx-engenharia-portfolio) repository**
>
> - 📄 Only static files are versioned there
> - 🔗 Always reference the toolbox for scripts and automations
> - 📚 See this README for usage examples and integration 

## 📖 More Documentation

- [DOCKER.md](DOCKER.md): Docker usage and guidelines
- [CONTRIBUTING.md](CONTRIBUTING.md): Contribution guidelines
- [CHANGELOG.md](CHANGELOG.md): Toolbox changelog (not for static content repositories)

## 🧪 Automated Testing

Automated tests ensure the integrity of the static HTML generation process. Tests validate the structure of portfolio.json, the generation of index.html, and the presence of key HTML elements and SEO tags.

### Running tests

Install test dependencies:
```bash
pip install -r requirements.txt
pip install pytest beautifulsoup4
```

Run the tests:
```bash
pytest test_generate_static_html.py
```

Tests will:
- Validate the structure of portfolio.json
- Run the static HTML generator
- Check the generated HTML for main sections, project cards, SEO meta tags, and image alt attributes

All tests must pass before deploying or merging changes. 