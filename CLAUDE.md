# CLAUDE.md

Notas para asistentes de IA trabajando en este repo. Mantener este archivo **breve**.

## Stack

- **Slides teoría:** Quarto (`.qmd`) → reveal.js (HTML). Config global en `_quarto.yml`. Tema en `slides/_theme/komorebi.scss`.
- **Prácticas:** Jupyter notebooks (`.ipynb`) en `notebooks/`.
- **Gestión de dependencias:** `uv`. Python 3.13. Ver `pyproject.toml`.
- **Idioma:** español.

## Convenciones

- Una carpeta por sesión, tanto en `slides/` como en `notebooks/`.
- Datos crudos en `data/raw/` (versionados; los procesados en `data/processed/` no).

## Comandos

```bash
uv sync                            # instalar/actualizar entorno
uv run jupyter lab                 # arrancar notebooks
quarto render slides/sesion1/sesion1.qmd  # renderizar una sesión
quarto preview slides/sesion1/sesion1.qmd # preview en vivo
```

> **En terminal Windows** Activar el venv (`.\.venv\Scripts\activate`) o establecer variable entorno `$env:QUARTO_PYTHON = ".\.venv\Scripts\python.exe"` antes de `quarto render` o `preview`. **En Vscode**, seleccionar el intérprete de Python del venv con Ctrl+Shift+P, `Python: Select Interpreter`.

## Cómo colaborar con el usuario

- **No hacer cambios a menos que se pidan explícitamente.** Muchas veces el usuario sólo está preguntando o discutiendo — responder con análisis, números, o explicación, no con ediciones. Cuando quiera que se cambie algo lo dirá explícitamente ("haz X", "edita Y", "añade Z"). Ante la duda, preguntar antes de editar.

## Flujo de trabajo con slides (Quarto)

- **NUNCA** ejecutar `quarto render` tras editar un `.qmd` — es lento. Para ver los cambios se usa siempre `quarto preview` (hot-reload).
- **Una vez por sesión**, comprobar si ya hay un servidor `quarto preview` corriendo:
  - En Windows: `Get-NetTCPConnection -State Listen` + `Get-CimInstance Win32_Process` para localizar el proceso `deno` que ejecuta `quarto.js preview` y su puerto.
  - Si está corriendo → anotar el puerto en el contexto de la sesión y **no volver a comprobarlo** en esa sesión. Asumir que cualquier edición a un `.qmd` se verá reflejada ahí.
  - Si no está corriendo → arrancarlo en segundo plano con `quarto preview <archivo>.qmd` (usar `run_in_background`).
- Después de editar el tema `slides/_theme/komorebi.scss`, `quarto preview` **no** hace hot-reload. Disparar un rebuild manual modificando el mtime con `(Get-Item slides/sesionN/sesionN.qmd).LastWriteTime = Get-Date`
- Para inspeccionar visualmente una slide, usar el skill **`playwright-cli`** apuntando a `http://localhost:<puerto>` (el puerto guardado al inicio de la sesión). Nunca renderizar a fichero para mirarlo.
- **Screenshots de `playwright-cli`:** guardarlos siempre en `.screenshots/` (carpeta gitignored, **nunca** en la raíz del repo ni en `slides/`) y **borrarlos en cuanto se hayan inspeccionado** — no acumular PNGs entre turnos. Si se necesita comparar antes/después, borrar ambos al terminar.
- **Numeración de slides: el usuario usa 1-based, las URLs son 0-based.** Si el usuario dice "slide 14", la URL es `http://localhost:<puerto>/slides/sesionN/sesionN.html#/13` (restar 1). Al referirse a una slide en la conversación, usar siempre el número 1-based del usuario.
- **Tras CUALQUIER cambio a una slide, verificar visualmente con `playwright-cli` que la slide no se desborda** (texto/figuras cortadas, scroll). Si se desborda, recortar texto, dividir en dos slides, o usar `{.large-fig}` / clases similares. No dar el cambio por terminado sin esta verificación.
