# scribble
Scribble.io from scratch


## Dev Setup

### 1. Install UV (Package Manager for Python)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Sync UV (Installs the Virtual environment and dependancies)
```bash
cd scribble
uv sync
```

### 4. Running the Application
This will generate datamodels from protobufs, run linter, formatter using ruff and run the main file.
```bash
uv run dev
```