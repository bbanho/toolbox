#!/usr/bin/env python3
"""
Generate static HTML for the portfolio site from portfolio.json using a Jinja2 template.
Optionally enriches data via AI agent (local or remote) if --use-ai is passed.

Usage:
    python generate_static_html.py [--use-ai]

Requirements:
    - Jinja2
    - Python 3.8+

Place this script in the toolbox directory. Run from the project root or specify paths as needed.
"""
import json
import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Optional: import your AI enrichment function here
# from ai_enrichment import enrich_portfolio_data

def load_portfolio(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def enrich_with_ai(data):
    # Placeholder for AI enrichment logic
    # Example: return enrich_portfolio_data(data)
    print("[INFO] AI enrichment is not implemented. Returning original data.")
    return data

def render_html(portfolio_data, template_path, output_path):
    env = Environment(loader=FileSystemLoader(template_path.parent))
    template = env.get_template(template_path.name)
    html = template.render(portfolio=portfolio_data)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[SUCCESS] HTML generated at {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate static HTML from portfolio.json")
    parser.add_argument('--use-ai', action='store_true', help='Enrich portfolio data using AI agent (optional)')
    parser.add_argument('--json', type=Path, default=Path('../pyx-engenharia-portfolio/portfolio.json'), help='Path to portfolio.json')
    parser.add_argument('--template', type=Path, default=Path('portfolio_template.html'), help='Path to Jinja2 template')
    parser.add_argument('--output', type=Path, default=Path('../pyx-engenharia-portfolio/index.html'), help='Output HTML file')
    args = parser.parse_args()

    data = load_portfolio(args.json)
    if args.use_ai:
        data = enrich_with_ai(data)
    render_html(data, args.template, args.output)

if __name__ == '__main__':
    main() 