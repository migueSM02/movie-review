# movie-review
Este proyecto, implementado en Flask, utiliza un modelo entrenado con el dataset imdb de keras para determinar si una reseña de película es positiva o negativa. Además, incorpora la librería googletrans para traducir automáticamente las reseñas al inglés, permitiendo que el modelo funcione sin importar el idioma en el que se ingrese la reseña original.

![vista](https://github.com/migueSM02/movie-review/assets/103807238/c5bfc7b6-01dc-4595-94db-554a1ad05583)

## Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/migueSM02/movie-review
```

### 2. crear el entorno virtual

```
cd movie-review
```
```
python -m venv venv
```
```
venv\Scripts\activate
```

### 3. Instalar Dependencias
```
pip install -r requirements.txt
```

### 4. Iniciar la Aplicación
```
python app.py
```

La aplicacion estara disponible en http://127.0.0.1:5000
