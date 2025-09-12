# Dijkstra Flask App

A small Flask web app that computes the shortest path between cities in Senegal using Dijkstra's algorithm and renders the result via simple HTML templates.

## Features
- Compute shortest path and total distance between two cities
- Minimal UI with Bootstrap
- Fast load times via HTTP compression and static asset caching

## Project Structure
```
app.py                # Flask app, routes, and performance config
dijkstra.py           # Graph utilities and Dijkstra algorithm
templates/
  index.html          # Form to input start and end cities
  chemin.html         # Results page with path and distance
static/
  css/styles.css      # Global and page-specific styles
requirements.txt      # Python dependencies
Procfile              # Gunicorn entry for deployment
README.md             # This file
```

## How It Works
- `dijkstra.py` defines an undirected weighted graph and the Dijkstra routine.
- `app.py` embeds a city distance graph, exposes two routes, and renders templates:
  - `/` GET: Show the form
  - `/chemin` POST: Compute shortest path and render results
- Templates are simple Jinja2 pages styled with Bootstrap.

## Setup
Create a virtual environment and install dependencies:
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Run the development server:
```bash
FLASK_APP=app.py flask run
```

Or start with Gunicorn:
```bash
gunicorn app:app
```

## Performance Optimizations
- HTTP compression via Flask-Compress
- Aggressive caching for static files (1 year, immutable)
- Cache-busting with `?v={{ STATIC_VERSION }}` on CSS
- Cleaned HTML heads (charset/viewport, preconnect) and consolidated CSS

## Notes
- The city graph is static in `app.py` for simplicity.
- For larger datasets or dynamic graphs, consider persisting data externally.
