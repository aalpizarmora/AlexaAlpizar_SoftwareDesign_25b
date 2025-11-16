# Patrón Decorator

Agrega funcionalidades adicionales a objetos de forma dinámica y flexible sin modificar su estructura base.

Funciones que cumple en el código:

- Los clientes pueden agregar ingredientes extra.

- Se pueden mezclar decoradores en cualquier orden.

- Cada decorador incrementa el costo automáticamente.

- Extensibilidad: Fácil agregar nuevos ingredientes (nuevos decoradores).

# Patrón Command

Encapsula solicitudes como objetos, separando quién pide la acción de quién la ejecuta.

Funciones que cumple dentro del codigo:

- No se depende de Barista/Pastelero directamente y el sistema no sabe cómo se preparan las cosas.

- Todos los comandos tienen la misma interfaz (ejecutar()).

- Los comandos se pueden encolar y ejecutar.

- Flexibilidad: Fácil agregar nuevos tipos de comandos sin modificar el sistema.

##
Decorator → Personaliza QUÉ se pide.

Command → Define CÓMO se ejecuta.
##

Estudiante: Alexa Alpízar Mora C20281