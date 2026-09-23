# dsa-study

A multi-language study of algorithms and data structures, written for learning.

## Layout

- One top-level directory per language (`python/`, `go/`, `rust/`, …).
- Each language directory is self-contained: its own toolchain config, dependencies, `.gitignore` entries and test runner. Don't share code or config across languages.
- Within a language, follow that language's normal project layout and naming.

## Conventions

- Clarity over cleverness. Implementations are for study, so prefer readable code with brief comments on the key idea and complexity (time/space).
- Every implementation gets tests in the language's standard test framework.
- Use the same algorithm/structure names across languages so implementations are easy to compare.

## Python (`python/`)

- Managed with uv. Run everything from `python/` via `uv run` (`uv run pytest`, `uv run ruff check .`, `uv run ruff format .`). Add deps with `uv add` / `uv add --dev`, never pip.
- Package `dsa` in src layout: `src/dsa/<category>/<name>.py`, tests mirrored at `tests/<category>/test_<name>.py`.
- Type-hint public functions. Run tests and ruff before committing.
