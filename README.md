## Install dependencies

```bash
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

# or, if using uv

uv sync
```

Run snake_screen with '-m' (to run as a module)

```bash
python3 -m snake.main

# or, if using uv

uv run python3 -m snake.main
```
