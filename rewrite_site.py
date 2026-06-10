from pathlib import Path

index = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HealthFit Training</title>
    <link rel="stylesheet" href="style.css">
    <script defer src="script.js"></script>
</head>
<body>

<header class="topbar">
    <div class="brand">
        <span class="logo-emoji">🏋️</span>
        <strong>HealthFit Training</strong>
    </div>

    <nav class="main-nav">
        <a href="#inicio">Inicio</a>
        <a href="#rutinas">Rutinas</a>
        <a href="#perfil">Perfil</a>
        <a href="#tema">Tema</a>
        <a href="#ayuda">Ayuda</a>
        <a href="#contacto">Contacto</a>
    </nav>

    <button id="theme-toggle" class="theme-toggle" type="button">Modo oscuro</button>
</header>

<main>
    <section id="inicio" class="hero">
        <div class="hero-copy">
            <p class="eyebrow">Bienvenido a tu gimnasio digital</p>
            <h1 class="hero-title">Entrena con foco, organiza tu perfil y cambia de tema al momento.</h1>
            <p class="hero-text">HealthFit Training es una web práctica para planificar tus rutinas, ajustar tu perfil personal y consultar ayuda rápida cuando la necesites.</p>
            <div class="hero-actions">
                <a href="#rutinas" class="btn btn-primary">Ver rutinas</a>
                <a href="#perfil" class="btn btn-secondary">Configurar perfil</a>
            </div>
        </div>

        <div class="hero-cards">
            <div class="small-card">
                <h3>Seguimiento</h3>
                <p>Lleva control de tus sesiones y tu progreso.</p>
            </div>
            <div class="small-card">
                <h3>Motivación</h3>
                <p>Encuentra ideas nuevas para entrenar cada semana.</p>
            </div>
        </div>
    </section>

    <section id="rutinas" class="section-block">
        <div class="section-header">
            <p class="section-label">Programa</p>
            <h2 class="section-title">Rutinas recomendadas</h2>
            <p>Escoge el tipo de entrenamiento que mejor se adapta a tu día.</p>
        </div>

        <div class="section-grid">
            <article class="card">
                <h3 class="card-title">Rutina básica</h3>
                <ul class="feature-list">
                    <li>15 sentadillas</li>
                    <li>10 flexiones</li>
                    <li>20 abdominales</li>
                    <li>30 segundos de plancha</li>
                </ul>
                <a href="#perfil" class="btn btn-link">Ir a perfil</a>
            </article>

            <article class="card">
                <h3 class="card-title">Rutina intermedia</h3>
                <ul class="feature-list">
                    <li>20 sentadillas</li>
                    <li>15 flexiones</li>
                    <li>30 abdominales</li>
                    <li>1 minuto de plancha</li>
                </ul>
                <a href="#tema" class="btn btn-link">Cambiar tema</a>
            </article>

            <article class="card">
                <h3 class="card-title">Rutina avanzada</h3>
                <ul class="feature-list">
                    <li>25 sentadillas con salto</li>
                    <li>20 flexiones</li>
                    <li>40 abdominales</li>
                    <li>1:30 minutos de plancha</li>
                </ul>
                <a href="#ayuda" class="btn btn-link">Ver ayuda</a>
            </article>
        </div>
    </section>

    <section id="perfil" class="section-block section-alt">
        <div class="section-header">
            <p class="section-label">Cuenta</p>
            <h2 class="section-title">Configuración de perfil</h2>
            <p>Personaliza tu información y objetivos para un entrenamiento más claro.</p>
        </div>

        <div class="profile-card">
            <div class="profile-info">
                <label>Nombre
                    <input type="text" value="Juan Pérez" readonly>
                </label>
                <label>Objetivo
                    <select>
                        <option>Tonificar</option>
                        <option selected>Perder peso</option>
                        <option>Ganar fuerza</option>
                    </select>
                </label>
                <label>Nivel
                    <input type="text" value="Intermedio" readonly>
                </label>
            </div>
            <div class="profile-summary">
                <h3>Resumen rápido</h3>
                <p>Tienes sesiones programadas 3 veces por semana y ayudas disponibles para mejorar cada entrenamiento.</p>
                <div class="profile-actions">
                    <button class="btn btn-primary">Editar perfil</button>
                    <button class="btn btn-secondary">Ver progreso</button>
                </div>
            </div>
        </div>
    </section>

    <section id="tema" class="section-block">
        <div class="section-header">
            <p class="section-label">Apariencia</p>
            <h2 class="section-title">Cambio de tema</h2>
            <p>Activa el modo oscuro cuando entrenes de noche o quieres descansar la vista.</p>
        </div>

        <div class="theme-card">
            <p>Presiona el botón de arriba para alternar entre el tema claro y el tema oscuro.</p>
            <div class="theme-preview">
                <span>Claro</span>
                <span>Oscuro</span>
            </div>
        </div>
    </section>

    <section id="ayuda" class="section-block section-alt">
        <div class="section-header">
            <p class="section-label">Soporte</p>
            <h2 class="section-title">Ayuda rápida</h2>
            <p>Respuestas a dudas comunes para sacar el máximo provecho del sitio.</p>
        </div>

        <div class="section-grid">
            <article class="card">
                <h3 class="card-title">¿Cómo empiezo?</h3>
                <p>Selecciona una rutina básica e intenta completar los ejercicios con buena técnica.</p>
            </article>
            <article class="card">
                <h3 class="card-title">¿Puedo cambiar mi objetivo?</h3>
                <p>Sí, puedes editar tu perfil y elegir un nuevo objetivo cuando lo necesites.</p>
            </article>
            <article class="card">
                <h3 class="card-title">¿Cómo activo el modo oscuro?</h3>
                <p>Haz clic en el botón "Modo oscuro" en la parte superior de la página.</p>
            </article>
        </div>
    </section>

    <section id="contacto" class="section-block">
        <div class="section-header">
            <p class="section-label">Contacto</p>
            <h2 class="section-title">¿Tienes una pregunta?</h2>
            <p>Escríbenos y te responderemos con consejos para tu entrenamiento.</p>
        </div>

        <div class="contact-card card">
            <p>Correo: info@healthfit.com</p>
            <p>Teléfono: +507 6000-0000</p>
            <a href="mailto:info@healthfit.com" class="btn btn-primary">Enviar correo</a>
        </div>
    </section>
</main>

<footer class="page-footer">
    <p>© 2026 HealthFit Training</p>
</footer>

</body>
</html>'''

style = '''html {
    scroll-behavior: smooth;
}

:root {
    --bg: #f5f7ff;
    --surface: rgba(255, 255, 255, 0.95);
    --surface-strong: #f8f9ff;
    --text: #111827;
    --muted: #4b5563;
    --accent: #2563eb;
    --accent-soft: rgba(37, 99, 235, 0.1);
    --border: rgba(15, 23, 42, 0.08);
    --shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
}

body {
    margin: 0;
    min-height: 100vh;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: var(--text);
    background: radial-gradient(circle at top left, rgba(59, 130, 246, 0.16), transparent 32%),
                linear-gradient(180deg, #eff6ff 0%, #f8fafc 60%, #ffffff 100%);
}

body.dark-theme {
    background: radial-gradient(circle at top left, rgba(96, 165, 250, 0.14), transparent 34%),
                linear-gradient(180deg, #0f172a 0%, #111827 50%, #0b1120 100%);
    color: #e2e8f0;
}

* {
    box-sizing: border-box;
}

img {
    max-width: 100%;
    display: block;
}

button,
input,
select,
a {
    font: inherit;
}

.topbar {
    position: sticky;
    top: 0;
    width: 100%;
    z-index: 20;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding: 16px 24px;
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
}

body.dark-theme .topbar {
    background: rgba(6, 10, 23, 0.9);
}

.brand {
    display: flex;
    align-items: center;
    gap: 10px;
    color: var(--text);
}

.logo-emoji {
    font-size: 1.3rem;
}

.main-nav {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    align-items: center;
}

.main-nav a {
    color: var(--muted);
    text-decoration: none;
    transition: color 0.25s ease;
}

.main-nav a:hover,
.main-nav a:focus-visible {
    color: var(--accent);
}

.theme-toggle {
    border: 1px solid var(--border);
    padding: 10px 16px;
    border-radius: 999px;
    background: white;
    color: var(--text);
    cursor: pointer;
    transition: background 0.25s ease, transform 0.2s ease;
}

body.dark-theme .theme-toggle {
    background: rgba(255, 255, 255, 0.08);
    color: #e2e8f0;
    border-color: rgba(148, 163, 184, 0.3);
}

.theme-toggle:hover {
    transform: translateY(-1px);
}

main {
    padding: 24px;
    max-width: 1200px;
    margin: 0 auto;
}

.hero {
    display: grid;
    grid-template-columns: 1.3fr 0.9fr;
    gap: 24px;
    align-items: center;
    margin-bottom: 32px;
    padding: 40px 0;
}

.hero-copy {
    padding: 32px;
    background: var(--surface);
    border-radius: 32px;
    box-shadow: var(--shadow);
}

.hero-title {
    font-size: clamp(2rem, 2.5vw, 3rem);
    line-height: 1.05;
    margin: 16px 0 18px;
}

.eyebrow {
    margin: 0;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #2563eb;
    font-size: 0.86rem;
}

.hero-text {
    line-height: 1.8;
    color: var(--muted);
    margin: 0 0 24px;
}

.hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}

.hero-cards {
    display: grid;
    gap: 16px;
}

.small-card {
    background: var(--surface-strong);
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 24px;
}

.small-card h3 {
    margin: 0 0 8px;
}

.section-block,
.card,
.profile-card,
.theme-card,
.contact-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 24px;
    box-shadow: var(--shadow);
}

.section-block {
    padding: 32px;
    margin-bottom: 32px;
}

.section-alt {
    background: rgba(255, 255, 255, 0.88);
}

body.dark-theme .section-alt,
body.dark-theme .section-block,
body.dark-theme .card,
body.dark-theme .profile-card,
body.dark-theme .theme-card,
body.dark-theme .contact-card,
body.dark-theme .small-card {
    background: rgba(15, 23, 42, 0.82);
    border-color: rgba(148, 163, 184, 0.16);
}

.section-header {
    max-width: 700px;
    margin-bottom: 24px;
}

.section-label {
    margin: 0 0 8px;
    color: #2563eb;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    font-size: 0.78rem;
}

.section-title {
    margin: 0 0 12px;
    font-size: 2rem;
}

.section-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 24px;
}

.card {
    padding: 24px;
}

.card-title {
    margin: 0 0 14px;
    color: var(--accent);
    font-size: 1.15rem;
}

.feature-list {
    padding-left: 18px;
    margin: 0 0 18px;
    color: var(--muted);
}

.feature-list li {
    margin-bottom: 8px;
}

.profile-card {
    display: grid;
    grid-template-columns: 2fr 1.2fr;
    gap: 24px;
    padding: 24px;
    align-items: start;
}

.profile-info,
.profile-summary {
    display: grid;
    gap: 14px;
}

.profile-info label {
    display: grid;
    gap: 8px;
    color: var(--muted);
}

.profile-info input,
.profile-info select {
    width: 100%;
    border-radius: 14px;
    border: 1px solid var(--border);
    padding: 12px 14px;
    background: white;
}

body.dark-theme .profile-info input,
body.dark-theme .profile-info select {
    background: rgba(15, 23, 42, 0.72);
    color: #e2e8f0;
    border-color: rgba(148, 163, 184, 0.22);
}

.profile-summary h3 {
    margin: 0 0 14px;
}

.profile-actions {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.theme-card,
.contact-card {
    padding: 24px;
}

.theme-preview {
    display: flex;
    gap: 10px;
    margin-top: 18px;
}

.theme-preview span {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 100px;
    padding: 12px 14px;
    border-radius: 14px;
    background: var(--surface-strong);
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 12px 20px;
    border-radius: 999px;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.btn:hover,
.btn:focus-visible {
    transform: translateY(-1px);
}

.btn-primary {
    background: var(--accent);
    color: white;
    box-shadow: 0 14px 30px rgba(37, 99, 235, 0.18);
}

.btn-secondary {
    background: transparent;
    border: 1px solid var(--accent);
    color: var(--accent);
}

.btn-link {
    display: inline-block;
    background: transparent;
    color: var(--accent);
    text-decoration: underline;
    padding: 0;
}

.page-footer {
    padding: 20px 24px;
    text-align: center;
    color: var(--muted);
}

footer a {
    color: inherit;
}

@media (max-width: 980px) {
    .hero {
        grid-template-columns: 1fr;
    }

    .profile-card {
        grid-template-columns: 1fr;
    }

    .main-nav {
        justify-content: center;
    }
}

@media (max-width: 680px) {
    .topbar {
        flex-direction: column;
        align-items: stretch;
    }

    .hero-copy,
    .hero-cards,
    .section-block {
        padding: 24px;
    }

    .theme-preview {
        flex-direction: column;
    }
}
'''

Path('index.html').write_text(index, encoding='utf-8')
Path('style.css').write_text(style, encoding='utf-8')
