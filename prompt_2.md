Prompt enviado: "Genera un archivo HTML llamado templates/map.html para la app 'Tijuana Café Guide'.

Requerimientos Técnicos:

Incluye Leaflet.js y Tailwind CSS vía CDN.

Incluye FontAwesome para íconos.

Crea un Navbar superior simple (Logo y enlace a 'Inicio') consistente con la fase anterior.

Debajo del Navbar, un contenedor div id='map' que ocupe el resto de la altura de la pantalla (calc(100vh - navbar)).

Inicializa el mapa centrado en Tijuana (Coordenadas: 32.5149, -117.0382) con un zoom de 13.

Usa tiles de OpenStreetMap.

Requerimientos UX (Ley de Fitts):

IMPORTANTE: Configura el mapa para que los controles de Zoom (zoomControl: false al inicio) se agreguen manualmente en la posición 'bottomright' (esquina inferior derecha) para facilitar el alcance en móviles.

Crea un botón flotante personalizado encima de los controles de zoom que sea para 'Mi Ubicación' (icono de target/brújula)."