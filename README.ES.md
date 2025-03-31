# Gatekeeper 🔒🚪

Este fue un pequeño proyecto personal que hice para mí mientras intentaba superar mis límites intentando algo nuevo que mi servidor necesitaba en ese momento.

## Hecho con ⚙️

* Nextcord
* Python
* python-dotenv

## Descripción 📜

Gatekeeper es un bot de Discord personalizado construido utilizando la librería Nextcord. Sirve como un bot de verificación para servidores de Discord, asegurando que los usuarios tengan dos roles específicos antes de otorgarles el rol de verificado y permitirles el acceso completo al servidor. Este bot monitorea continuamente los roles de los usuarios en busca de cambios para automatizar el proceso de verificación.

## Cómo usar 🚀

1.  **Prerrequisitos:**
    * Python 3.7 o superior
    * Librería Nextcord instalada (`pip install nextcord`)
    * Librería `python-dotenv` instalada (`pip install python-dotenv`)

2.  **Configuración:**
    * Clona este repositorio en tu máquina local o instancia en la nube.
    * Crea un archivo `.env` en el directorio raíz del proyecto.
    * Agrega las siguientes variables de entorno al archivo `.env`, reemplazando los valores de marcador de posición con tu token de bot de Discord real, el ID del servidor y los IDs de los dos roles requeridos y el rol de verificado:

        ```env
        discord_bot_token = "insert_bot_token_here"
        guild_id = "insert_guild_id_here"
        role1 = "insert_role_id_here"
        role2 = "insert_role_id_here"
        verified_role_id = "insert_role_id_here"
        unverified_role = "insert_role_id_here"
        ```

        **Nota:** Necesitarás obtener tu token de bot del Portal de Desarrolladores de Discord y los IDs del servidor y los roles de tu servidor de Discord.

3.  **Ejecutando el Bot:**

    * **Localmente:** Abre tu terminal o símbolo del sistema, navega al directorio del proyecto y ejecuta el bot utilizando el siguiente comando:

        ```bash
        python Gatekeeper.py
        ```

    * **Despliegue en la Nube (Recomendado):** Para un funcionamiento continuo las 24 horas del día, los 7 días de la semana, se recomienda desplegar este bot en una plataforma de alojamiento en la nube como Heroku, AWS, Google Cloud o servicios similares (en mi caso utilicé Discloud). Sigue las instrucciones de despliegue específicas de la plataforma, asegurándote de que tu archivo `.env` esté configurado correctamente en el entorno de la nube.

## Licencia 📄

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

##
Hecho con ❤️ por Texdroid
