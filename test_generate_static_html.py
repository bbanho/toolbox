#!/usr/bin/env python3
"""
Automated tests for static HTML generation from portfolio.json using generate_static_html.py.

Usage:
    pytest test_generate_static_html.py

Requirements:
    - pytest
    - beautifulsoup4
    - Python 3.8+
"""
import json
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup
import pytest

PORTFOLIO_JSON = Path('../pyx-engenharia-portfolio/portfolio.json')
TEMPLATE = Path('portfolio_template.html')
OUTPUT_HTML = Path('../pyx-engenharia-portfolio/index.html')
SCRIPT = Path('generate_static_html.py')

# --- JSON Validation ---
def test_portfolio_json_exists():
    assert PORTFOLIO_JSON.exists(), f"{PORTFOLIO_JSON} not found"

def test_portfolio_json_structure():
    with open(PORTFOLIO_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert isinstance(data, dict), "portfolio.json should be a dict at the top level"
    for categoria, projetos in data.items():
        assert isinstance(projetos, list), f"Category {categoria} should be a list"
        for item in projetos:
            assert 'empresas' in item or 'itens' in item, f"Each item in {categoria} should have 'empresas' or 'itens'"

# --- HTML Generation ---
def test_generate_html_runs():
    result = subprocess.run(['python3', str(SCRIPT)], capture_output=True, text=True)
    assert result.returncode == 0, f"generate_static_html.py failed: {result.stderr}"
    assert OUTPUT_HTML.exists(), "index.html was not generated"

# --- HTML Content Validation ---
def test_html_content():
    with open(OUTPUT_HTML, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    # Check for main sections
    assert soup.find('section', {'id': 'portfolio'}), "Portfolio section missing"
    # Check for at least one project card
    assert soup.find(class_='project-card'), "No project cards found"
    # Check for meta tags SEO
    assert soup.find('meta', {'name': 'description'}), "Meta description missing"
    assert soup.find('meta', {'property': 'og:title'}), "OG title missing"
    # Check for images with alt
    imgs = soup.find_all('img')
    assert any(img.get('alt') for img in imgs), "Some images missing alt attribute"

# --- Clean up (optional) ---
# def teardown_module(module):
#     if OUTPUT_HTML.exists():
#         OUTPUT_HTML.unlink() 