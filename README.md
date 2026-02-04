# CoffeeRoute 
# Tijuana Café Guide

> **Descubre el verdadero café de especialidad.**
> Una guía interactiva curada para encontrar las mejores barras locales, diseñada con accesibilidad y experiencia de usuario en mente.

## Cómo correr el proyecto localmente

1.  **Clonar el repositorio:**
    ```bash
    git clone [TU_LINK_DEL_REPO]
    cd tijuana_cafe_map
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar el servidor:**
    ```bash
    python app.py
    ```
4.  Abrir en el navegador: `http://127.0.0.1:5000`

---

## Stack Tecnológico

* **Backend:** Python 3 + Flask.
* **Frontend:** HTML5, Tailwind CSS (vía CDN).
* **Mapas:** Leaflet.js + OpenStreetMap.
* **Iconos:** FontAwesome.
* **IA de Soporte:** Gemini Canvas (Generación de código y consultoría UX).

---

## Justificación de Diseño (UX/UI)

Este proyecto no es solo un mapa, es un ejercicio de UX aplicado. Decisiones clave:

### 1. Ley de Fitts & Ergonomía Móvil
Los controles de mapa suelen estar arriba a la izquierda (difíciles de alcanzar en móviles).
* **Decisión:** Movimos los controles de Zoom y "Mi Ubicación" a la **esquina inferior derecha**.
* **Resultado:** Mayor facilidad de uso con el pulgar.

### 2. Feedback del Sistema (Heurística de Nielsen)
El usuario necesita saber qué está pasando.
* **Latencia:** Al guardar un punto, simulamos una espera de 1.5s mostrando un **Spinner de carga** ("Guardando...").
* **Confirmación:** Al finalizar, usamos una notificación tipo **Toast** no intrusiva.
* **Prevención de Errores:** Botón explícito de "Cancelar" para borrar marcadores accidentales.

### 3. Accesibilidad y Vistas Alternativas
No todos pueden interactuar con un mapa visual.
* **Vista Dual:** Implementamos una lista lateral sincronizada.
* **Sincronización:** Clic en la lista hace `FlyTo` (vuelo suave) hacia el marcador.
* **ARIA Labels:** Se etiquetaron botones de íconos para lectores de pantalla.

---

## Créditos a la IA & Prompt Engineering

Este código fue co-creado utilizando **Gemini Canvas**. A continuación, el registro de los prompts clave que estructuraron la aplicación:

| Fase | Objetivo | Prompt Principal (Resumido) |
| **1** | **Landing Page** | *"Crea una Landing Page HTML con Tailwind. Hero Section con imagen de café, título 'Descubre el Verdadero Café'. Estilo minimalista/tostado."* |
| **2** | **Mapa Base** | *"Genera un HTML con Leaflet.js. IMPORTANTE: Mueve los controles de zoom a 'bottomright' (Ley de Fitts) y añade un botón personalizado de 'Mi Ubicación'."* |
| **3** | **Feedback** | *"Script JS para Leaflet: Al clic, marcador temporal con popup. Al guardar, mostrar spinner 'Guardando...', usar fetch a Flask, y mostrar Toast de éxito."* |
| **4** | **Accesibilidad** | *"Modifica el layout a 2 columnas (Mapa + Lista). Al guardar punto, agrégalo a la lista lateral. Clic en lista hace FlyTo al mapa. Añade aria-labels."* |

---

## Licencia
Proyecto educativo realizado para la actividad "Desarrollo Asistido por IA".