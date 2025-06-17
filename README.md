# PYX Toolbox

A collection of development and maintenance tools for web projects.

## Tools

### Local Development Server (`local_server.py`)
A Python-based local development server with proper MIME types and error handling.
```bash
python local_server.py [-p PORT] [-d DIRECTORY]
```

### Image Optimizer (`optimize_images.py`)
Optimizes images for web use while maintaining quality.
```bash
python optimize_images.py DIRECTORY [-q QUALITY] [-w MAX_WIDTH]
```

### Web Validator (`validate_web.py`)
Validates HTML, accessibility, and performance metrics.
```bash
python validate_web.py [-u URL] [-p PATHS...] [-o OUTPUT]
```

### GitHub Commands (`gh_commands.sh`)
Common GitHub commands for project management.
```bash
./gh_commands.sh [command] [options]
```

## Requirements

- Python 3.8+
- pip packages:
  - Pillow
  - requests
  - beautifulsoup4
- Git
- GitHub CLI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pyx-toolbox.git
cd pyx-toolbox
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Make scripts executable:
```bash
chmod +x *.py *.sh
```

## Usage

Each tool has its own documentation in the script's docstring. Run any script with `--help` for usage information.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details 