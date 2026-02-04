# Bitácora de UX - Fase 2: Arquitectura del Mapa

## Objetivo
Implementar el mapa interactivo asegurando que la navegación sea accesible y no intrusiva.

## Decisiones de Diseño (UX)

### 1. Aplicación de la Ley de Fitts
**Observación:** En la librería Leaflet.js, los controles de zoom vienen por defecto en la esquina superior izquierda.
**Problema:** En dispositivos móviles (que es el caso de uso principal para buscar una cafetería estando en la calle), la esquina superior izquierda es la zona de más difícil acceso para el pulgar de un usuario diestro.
**Solución:** - Se movieron los controles de Zoom (`+` / `-`) a la esquina **inferior derecha** (`position: 'bottomright'`).
- Esto reduce la distancia ("D" en la fórmula de Fitts) que el dedo debe recorrer desde la posición de descanso natural, haciendo la interacción más rápida y cómoda.

### 2. Densidad de Información
- Se decidió utilizar un **mapa de pantalla completa** (Full Viewport) restando solo el espacio del Navbar.
- **Minimalismo:** No se agregaron paneles laterales ni menús flotantes en esta fase inicial. El mapa es el protagonista ("Hero") para evitar saturación cognitiva. El usuario entra y ve Tijuana inmediatamente, sin distracciones.

### 3. Feedback del Sistema
- Se agregó un botón visual de "Mi Ubicación" (icono de mira/crosshair) agrupado junto al zoom. Aunque funcionalmente aún no activa el GPS (pendiente para lógica JS futura), visualmente le indica al usuario que esa funcionalidad existe y dónde encontrarla.