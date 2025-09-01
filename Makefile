PYTHON ?= python3
PIP ?= pip3

.PHONY: setup install run dev clean

setup:
	$(PIP) install -r backend/requirements.txt

install: setup

run:
	uvicorn backend.app.main:app --host 0.0.0.0 --port 8000

dev:
	uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -delete

