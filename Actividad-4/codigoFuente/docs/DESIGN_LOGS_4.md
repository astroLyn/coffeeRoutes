# Bitácora de UX - Fase 4: Accesibilidad y Vistas Alternativas

## Objetivo
Hacer que la información del mapa sea accesible para usuarios que no pueden navegar espacialmente o prefieren datos estructurados.

## Mejoras de Accesibilidad (A11y) Implementadas

### 1. Alternativa Textual (Vista de Lista)
**Problema:** Un mapa es un componente puramente visual y espacial. Los lectores de pantalla (Screen Readers) tienen dificultad para interpretar "pines" dispersos.
**Solución:** Se implementó una **columna lateral (sidebar)** que muestra la misma información que el mapa pero en formato de texto secuencial.
- **Sincronización:** Al crear un punto, se agrega automáticamente a la lista.
- **Interacción Redundante:** Hacer clic en la lista lleva al usuario al lugar en el mapa (animación `flyTo`), permitiendo dos formas de navegación.

### 2. Etiquetado ARIA
**Problema:** Los botones con íconos (como la lupa o la mira) son invisibles para usuarios ciegos si no tienen etiquetas de texto.
**Solución:** Se agregaron atributos `aria-label` descriptivos:
- Botón de Ubicación: `aria-label="Centrar en mi ubicación actual"`
- Entradas de la lista: `aria-label="Ir a la ubicación de [Nombre del Café]"`

### 3. Contraste y Color
**Observación:** Se verificó que el texto de la lista tenga alto contraste (Texto oscuro sobre fondo blanco) y que los marcadores del mapa no se pierdan en el fondo.