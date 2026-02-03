Modifica el archivo templates/map.html. Cambia la estructura del body para tener un diseño de dos columnas usando Tailwind CSS:

Estructura:

Sidebar (Lista): Ocupa el 1/3 del ancho en escritorio (o 100% en móvil debajo del mapa). Debe tener un título 'Cafeterías Guardadas' y un contenedor vacío id='lista-lugares' con scroll vertical (overflow-y-auto).

Main (Mapa): Ocupa el 2/3 restantes.

Funcionalidad JS:

Crea una función agregarItemLista(data) que reciba los datos del punto guardado.

Esta función debe inyectar una tarjeta HTML en el sidebar con el nombre del café y las coordenadas.

Sincronización: Al hacer clic en esa tarjeta de la lista, el mapa debe ejecutar map.flyTo([lat, lng], 15) para llevar al usuario a ese punto.

Integra esta función dentro del bloque de 'success' de guardarPunto.

Accesibilidad: Asegúrate de agregar aria-label='Centrar mapa en mi ubicación' al botón de GPS y aria-label a los ítems de la lista.