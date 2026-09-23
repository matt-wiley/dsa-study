# dsa (Python)

Python implementations for [dsa-study](../README.md). Managed with [uv](https://docs.astral.sh/uv/).

## Layout

- `src/dsa/<category>/<name>.py`: implementations, grouped by category (e.g. `sorting/merge_sort.py`, `structures/linked_list.py`).
- `tests/<category>/test_<name>.py`: pytest tests that mirror the source layout.

## Commands

```sh
uv sync                  # create/update the venv
uv run pytest            # run all tests
uv run pytest -k merge   # run matching tests
uv run ruff check .      # lint
uv run ruff format .     # format
```
