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

## Instalando bibliotecas: REQUEST y PYTHON-DOTENV

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

## PASOS PARA GITHUB
Crear nuestro repositorio en GitHub
Ahora vamos a conectar nuestro proyecto local con GitHub.
Paso 10. Crear el repositorio remoto
1. Entra a GitHub.
2. Inicia sesión.
3. Haz clic en el botón New repository.
4. Configúralo así:
Configuración recomendada

Ejemplo de cómo crear tu repositorio.
Repository namepractica-programa-sincrono

DescriptionPrimera práctica de Python: programación síncrona y consumo de APIs.

Visibility
Public

Te recomiendo público para que puedas construir tu portafolio, siempre que revises que no haya información privada.
No selecciones Add README, Add .gitignore ni Add license. Ya estamos preparando esos archivos localmente.

Haz clic en Create repository.
Paso 11. Conectar VS Code con GitHub
GitHub te mostrará una página con instrucciones para conectar tu repositorio.

Nosotros utilizaremos los comandos de la sección de repositorio existente.

Primero, asegúrate de que tu rama principal se llame main:
git branch -M main


Después agrega la dirección de tu repositorio:
git remote add origin URL_DE_TU_REPOSITORIO


Sustituye el texto por la dirección HTTPS que te proporciona GitHub.

Finalmente:
git push -u origin main


Este último comando envía tus commits a GitHub.