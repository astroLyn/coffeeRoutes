Actualiza el script de map.html para manejar la creación de nuevos puntos con micro-interacciones de UX completas.

Requerimientos de Interacción:

Evento Clic: Al hacer clic en el mapa, coloca un marcador temporal inmediatamente (Feedback instantáneo).

Estado Inicial (Borrador): El marcador debe abrir un popup con dos botones: 'Cancelar' (borra el marcador) y 'Guardar'.

Estado de Carga (Latencia): Al hacer clic en 'Guardar', oculta los botones dentro del popup y muestra un spinner animado con el texto 'Guardando...' (para gestionar la espera del usuario).

Conexión Backend: Usa fetch para enviar los datos (lat, lng) al endpoint /guardar_punto mediante POST.

Estado de Éxito: Cuando el servidor responda 'success', cierra el popup y muestra una notificación flotante tipo 'Toast' en la parte inferior de la pantalla que diga '¡Café guardado con éxito!'.

Manejo de Errores: Si el usuario cierra el popup sin guardar, el marcador debe eliminarse automáticamente para no ensuciar el mapa.