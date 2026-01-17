# curso-python

Entorno base para el curso "Introducción a la Programación en Python".

## Requisitos

- Python >= 3.10 (recomendado 3.11)

## Instalación

### 1) Crear entorno con micromamba (recomendado)

```bash
micromamba create -n curso-python python=3.11
micromamba activate curso-python
```

Si micromamba no está disponible, puedes usar conda:

```bash
conda create -n curso-python python=3.11
conda activate curso-python
```

### 2) Instalar el proyecto

```bash
pip install -e .
```

### 3) Registrar el kernel

```bash
python -m ipykernel install --user --name curso-python
```

## Uso

### Ejecutar Jupyter

```bash
jupyter lab
```

### Usar RISE (presentaciones)

- En JupyterLab: habilita la extensión de `jupyterlab-rise`.
- En el notebook: View → Cell Toolbar → Slideshow.
- Inicia la presentación con `Alt+R`.
