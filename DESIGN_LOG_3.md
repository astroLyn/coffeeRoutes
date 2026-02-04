# Bitácora de UX - Fase 3: Micro-interacciones y Feedback

## Objetivo
Gestionar la incertidumbre del usuario durante la creación de datos (puntos en el mapa) y prevenir errores de entrada.

## Implementación de Feedback

### 1. Estado de "Carga" (Latencia)
**Problema:** Las conexiones móviles pueden ser lentas. Si el usuario da clic en "Guardar" y no ve respuesta, podría hacer clic múltiples veces (duplicando datos) o pensar que la app no sirve.
**Solución:** - Se implementó un estado intermedio en el Popup. Al dar clic en "Guardar", los botones desaparecen inmediatamente y se reemplazan por un **Spinner animado** con el texto "Guardando...".
- Esto confirma al usuario que su solicitud fue recibida y se está procesando.

### 2. Estado de "Éxito"
**Solución:** - Al recibir el `200 OK` del backend, se utiliza una notificación tipo **Toast** (mensaje flotante inferior).
- **Por qué Toast:** Es menos intrusivo que una alerta (`alert()`) y no requiere que el usuario haga clic para cerrarla, permitiendo que continúe navegando fluidamente.

### 3. Prevención de Errores (Heurística de Nielsen)
**Problema:** En pantallas táctiles es fácil tocar el mapa por error ("Fat finger syndrome").
**Solución:** - El marcador creado es "Temporal".
- El popup incluye explícitamente un botón **"Cancelar"** que elimina el marcador.
- Si el usuario cierra el popup sin guardar, el marcador se asume como error y se elimina automáticamente para mantener el mapa limpio.