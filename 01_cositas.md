# Programa síncrono
Este es un programita para ver el clima en veracruz y para ver una noticia relevante del dia, es una sencilla practica para comprender mejor la diferencia entre programación sincrona y asincrona, ademas de recordar el uso de APIs, git y github.

## Recordando Git

| Comando | ¿Qué hace? |
| --- | --- |
| `git init` | Inicializa un repositorio. |
| `git status` | Muestra el estado de los archivos. |
| `git add .` | Prepara los cambios para el commit. |
| `git commit -m "mensaje"` | Guarda una versión en el historial. |
| `git log` | Muestra el historial de commits. |
| `git push` | Sube los commits al repositorio remoto. |
| `git pull` | Obtiene e integra cambios del repositorio remoto. |
| `git clone` | Descarga una copia de un repositorio. |

## APIs
- **API(Aplication Programming Interface):** Conjunto de reglas y protocolos que permite que dos programas o aplicaciones diferentes se comuniquen entre sí para compartir datos y funciones.
- **Open-Meteo:** Integración de modelos meteorológicos de alta resolución con pronósticos de hasta 16 días. [Open-Meteo]("https://open-meteo.com/").

## Buenas practicas en GitHub
Además de tus archivos .py, existen tres archivos que son muy importantes en proyectos profesionales.

**A. README.md**
Es el documento que explica tu proyecto.
Cuando alguien entra a tu repositorio de GitHub, normalmente lo primero que verá será este archivo.

Un buen README debe responder:
- ¿Qué hace el proyecto?
- ¿Para qué fue creado?
- ¿Qué tecnologías utiliza?
- ¿Cómo se instala?
- ¿Cómo se ejecuta?
- ¿Qué funcionalidades tiene?

**B. .gitignore**
Este archivo le indica a Git qué archivos no debe incluir en el control de versiones.
¿Por qué es importante?

Porque no queremos subir:
- API Keys.
- Contraseñas.
- Entornos virtuales.
- Archivos temporales innecesarios.


**C. requirements.txt**
Este archivo contiene las dependencias de tu proyecto.
¿Para qué sirve?

Imagina que alguien descarga tu proyecto. Necesita saber qué bibliotecas debe instalar para ejecutarlo.

Con este archivo podrá instalar las dependencias mediante:

`pip install -r requirements.txt`

## Entorno virtual
Un entorno virtual es un espacio aislado que permite que cada proyecto tenga sus propias dependencias.

En la terminal de VS Code ejecuta:
`python -m venv .venv`

Ahora activa el entorno:
`.venv\Scripts\Activate.ps1`

## Instalando bibliotecas

`pip install requests python-dotenv`
¿Qué estamos instalando?

1. requests

Nos permitirá realizar solicitudes HTTP a Open-Meteo y GNews.

2. python-dotenv

Nos permitirá leer información privada guardada en un archivo .env, como nuestra API Key.

*comando:* `pip list`
Este comando muestra las bibliotecas instaladas en tu entorno virtual.

**variables de entorno**
Aquí necesitamos comprender dos herramientas:
- `load_dotenv()` : carga las variables almacenadas en .env.
- `os.getenv()` : permite recuperar el valor de una variable de entorno.

## mensajes clave en git
- feat: para nuevas funcionalidades.
- fix: para correcciones.
- docs: para documentación.
- refactor: para reorganización del código.

`pip freeze > requirements.txt` Esto registra las bibliotecas instaladas en tu entorno virtual.