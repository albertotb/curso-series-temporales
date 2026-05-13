# CLAUDE.md

Notas para asistentes de IA trabajando en este repo. Mantener este archivo **breve**.

## Stack (decisiones cerradas)

- **Slides teoría:** Quarto (`.qmd`) → reveal.js (HTML). Config global en `_quarto.yml`. Tema en `slides/_theme/komorebi.scss`.
- **Prácticas:** Jupyter notebooks (`.ipynb`) en `notebooks/sesion{1..4}/`.
- **Gestión de dependencias:** `uv`. Python 3.13. Ver `pyproject.toml`.
- **Idioma:** español.
- **Branding:** seguir guía Komorebi (paleta y tipografía ya en el SCSS).

## Comandos

```bash
uv sync                            # instalar/actualizar entorno
uv run jupyter lab                 # arrancar notebooks
quarto render slides/sesion1/sesion1.qmd  # renderizar una sesión
quarto preview slides/sesion1/sesion1.qmd # preview en vivo
```

> **En Windows** Quarto no encuentra el Jupyter del `.venv` porque busca `python3` y el venv solo trae `python.exe`. Activar el venv no lo arregla (solo cambia el `PATH`). Solución: indicarle el intérprete vía `QUARTO_PYTHON`. Una sola vez por usuario:
>
> ```powershell
> [Environment]::SetEnvironmentVariable("QUARTO_PYTHON", "$PWD\.venv\Scripts\python.exe", "User")
> ```
>
> O por sesión: `$env:QUARTO_PYTHON = ".\.venv\Scripts\python.exe"` antes de `quarto render`.

## Convenciones

- Una carpeta por sesión, tanto en `slides/` como en `notebooks/`.
- Datos crudos en `data/raw/` (no se versiona el contenido, solo `.gitkeep`).
- No commitear outputs de notebooks (usar `nbstripout`).
