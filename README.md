# HealthFit Training

Este proyecto es una página web estática de entrenamiento que incluye:

- Página de inicio con información y rutinas.
- Página de perfil para guardar nombre, correo y nivel.
- Página de ayuda.
- Botón para copiar el enlace de la web y compartirlo.
- Tema oscuro con cambio dinámico.

## Cómo publicar la página

### Opción 1: GitHub Pages
1. Crea un repositorio en GitHub.
2. Sube todos los archivos del proyecto al repositorio.
   - Puedes usar GitHub Desktop, la interfaz web de GitHub o `git` desde la terminal.
3. El proyecto ya incluye un flujo de despliegue en `.github/workflows/pages.yml`.
   - Este flujo publica automáticamente el contenido en la rama `gh-pages` cuando hagas `push` a `main`.
4. En la configuración del repositorio, activa GitHub Pages y selecciona la rama `gh-pages` como origen.
5. GitHub te dará una URL pública como `https://<tu-usuario>.github.io/<nombre-del-repo>/`.

> Con esto, la página será accesible desde cualquier navegador en Internet.

> Si usas el flujo automático, basta con hacer `git push origin main` y GitHub Actions generará la versión pública.
>
> Nota: este proyecto ya incluye un archivo `.nojekyll` para que GitHub Pages sirva los archivos estáticos directamente sin procesarlos con Jekyll.

### Opción 2: publicar con Netlify
1. Ve a https://app.netlify.com/ y crea una cuenta gratuita.
2. Haz clic en "New site from Git" si tienes el proyecto en GitHub, o usa "Deploy manually" y arrastra la carpeta del proyecto.
3. Netlify creará una URL pública para tu sitio.

### Opción 3: publicar con Vercel
1. Ve a https://vercel.com/ y crea una cuenta gratuita.
2. Conecta tu repositorio de GitHub o arrastra la carpeta del proyecto.
3. Vercel generará una URL pública automática.

### Vista previa local
Si solo necesitas ver la web en tu computador, usa un servidor local:

```bash
cd "c:\Users\PC\Documents\ProyectoDIU"
python -m http.server 8000
```

También puedes ejecutar el helper `serve.bat` desde la carpeta del proyecto:

```text
serve.bat
```

Si tienes problemas con Python o Node, usa PowerShell:

```text
powershell -NoProfile -ExecutionPolicy Bypass -File serve.ps1
```

Luego abre:

```text
http://localhost:8000
```

> Si quieres ver la página desde tu teléfono en la misma red Wi-Fi, usa la IP de tu PC en lugar de `localhost`.
> Por ejemplo: `http://192.168.50.221:8000/index.html`
> `localhost` funciona solo en el mismo equipo donde corre el servidor.
> Para que otras personas fuera de tu red puedan entrar, usa un hosting público como GitHub Pages, Netlify o Vercel.

## Cómo compartir la página

Si solo necesitas ver la web en tu computadora, abre el proyecto en un navegador o usa un servidor local:

```bash
cd "c:\Users\PC\Documents\ProyectoDIU"
python -m http.server 8000
```

Luego abre:

```text
http://localhost:8000
```

> Nota: `localhost` y los archivos `file://` solo funcionan en tu propia computadora. No son públicos ni accesibles desde otro dispositivo.
> Para que otras personas vean tu sitio, debes usar un hosting real como GitHub Pages, Netlify o Vercel.

### Opción 3: usar un servicio de hosting rápido

Puedes usar servicios gratuitos como:

- [GitHub Pages](https://pages.github.com/)
- [Netlify](https://www.netlify.com/)
- [Vercel](https://vercel.com/)

Solo arrastra la carpeta del proyecto o conecta el repositorio.

## Cómo compartir la página

- En la página principal, pulsa "Copiar enlace".
- O usa el botón "Compartir" si tu navegador es compatible.
- Luego pega el enlace en WhatsApp, correo, Instagram o cualquier red social.
