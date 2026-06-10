const themeToggle = document.getElementById('theme-toggle');
const profileForm = document.getElementById('profile-form');
const profileName = document.getElementById('profile-name');
const profileEmail = document.getElementById('profile-email');
const profileLevel = document.getElementById('profile-level');
const profileStatus = document.getElementById('profile-status');
const profileDisplayName = document.getElementById('profile-display-name');
const profileDisplayEmail = document.getElementById('profile-display-email');
const profileDisplayLevel = document.getElementById('profile-display-level');
const routineForm = document.getElementById('routine-form');
const routineDays = document.getElementById('routine-days');
const routineDuration = document.getElementById('routine-duration');
const routineFocus = document.getElementById('routine-focus');
const routineStatus = document.getElementById('routine-status');
const displayDays = document.getElementById('display-days');
const displayDuration = document.getElementById('display-duration');
const displayFocus = document.getElementById('display-focus');
const streakButton = document.getElementById('streak-button');
const streakCurrent = document.getElementById('streak-current');
const streakBest = document.getElementById('streak-best');
const streakLast = document.getElementById('streak-last');
const optionReminders = document.getElementById('option-reminders');
const optionUpdates = document.getElementById('option-updates');
const optionSounds = document.getElementById('option-sounds');
const copyLinkButton = document.getElementById('copy-link-button');
const shareButton = document.getElementById('share-button');
const shareStatus = document.getElementById('share-status');

const storagePrefix = 'healthfit';
const legacyStoragePrefix = 'powerfit';

const storageKey = (key) => `${storagePrefix}-${key}`;
const legacyStorageKey = (key) => `${legacyStoragePrefix}-${key}`;

const readStorage = (key) => {
    const current = localStorage.getItem(storageKey(key));
    if (current !== null) return current;
    return localStorage.getItem(legacyStorageKey(key));
};

const writeStorage = (key, value) => {
    localStorage.setItem(storageKey(key), value);
};

const applyTheme = (theme) => {
    const isDark = theme === 'dark';
    document.body.classList.toggle('dark-theme', isDark);
    if (themeToggle) {
        themeToggle.textContent = isDark ? 'Modo claro' : 'Modo oscuro';
    }
    localStorage.setItem('theme', theme);
};

const loadProfile = () => {
    const profile = JSON.parse(readStorage('profile') || '{}');
    if (profile.name) profileName.value = profile.name;
    if (profile.email) profileEmail.value = profile.email;
    if (profile.level) profileLevel.value = profile.level;
    updateProfileDisplay(profile);
};

const saveProfile = (event) => {
    event.preventDefault();
    const profile = {
        name: profileName.value.trim(),
        email: profileEmail.value.trim(),
        level: profileLevel.value,
    };
    writeStorage('profile', JSON.stringify(profile));
    profileStatus.textContent = 'Perfil guardado correctamente.';
    updateProfileDisplay(profile);
    setTimeout(() => {
        profileStatus.textContent = '';
    }, 3000);
};

const updateProfileDisplay = (profile) => {
    if (profileDisplayName) profileDisplayName.textContent = profile.name || '-';
    if (profileDisplayEmail) profileDisplayEmail.textContent = profile.email || '-';
    if (profileDisplayLevel) profileDisplayLevel.textContent = profile.level || '-';
};

const loadRoutineConfig = () => {
    const routine = JSON.parse(readStorage('routine') || '{}');
    if (routineDays && routine.days) routineDays.value = routine.days;
    if (routineDuration && routine.duration) routineDuration.value = routine.duration;
    if (routineFocus && routine.focus) routineFocus.value = routine.focus;
    if (displayDays) displayDays.textContent = routine.days ? `${routine.days} días` : '-';
    if (displayDuration) displayDuration.textContent = routine.duration ? `${routine.duration} min` : '-';
    if (displayFocus) displayFocus.textContent = routine.focus || '-';
};

const saveRoutineConfig = (event) => {
    event.preventDefault();
    const routine = {
        days: routineDays.value,
        duration: routineDuration.value,
        focus: routineFocus.value,
    };
    writeStorage('routine', JSON.stringify(routine));
    if (routineStatus) routineStatus.textContent = 'Configuración de rutina guardada.';
    loadRoutineConfig();
    setTimeout(() => {
        if (routineStatus) routineStatus.textContent = '';
    }, 3000);
};

const loadStreaks = () => {
    const streaks = JSON.parse(readStorage('streak') || '{}');
    if (streakCurrent) streakCurrent.textContent = streaks.current || 0;
    if (streakBest) streakBest.textContent = streaks.best || 0;
    if (streakLast) streakLast.textContent = streaks.last || '-';
};

const registerStreak = () => {
    const today = new Date().toLocaleDateString();
    const streaks = JSON.parse(readStorage('streak') || '{}');
    if (streaks.last === today) {
        return;
    }
    streaks.current = (streaks.current || 0) + 1;
    streaks.best = Math.max(streaks.best || 0, streaks.current);
    streaks.last = today;
    writeStorage('streak', JSON.stringify(streaks));
    loadStreaks();
};

const loadOptions = () => {
    const options = JSON.parse(readStorage('options') || '{}');
    if (optionReminders) optionReminders.checked = options.reminders || false;
    if (optionUpdates) optionUpdates.checked = options.updates || false;
    if (optionSounds) optionSounds.checked = options.sounds || false;
};

const saveOptions = () => {
    const options = {
        reminders: optionReminders ? optionReminders.checked : false,
        updates: optionUpdates ? optionUpdates.checked : false,
        sounds: optionSounds ? optionSounds.checked : false,
    };
    writeStorage('options', JSON.stringify(options));
};

const currentTheme = localStorage.getItem('theme') || 'light';
applyTheme(currentTheme);

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const nextTheme = document.body.classList.contains('dark-theme') ? 'light' : 'dark';
        applyTheme(nextTheme);
    });
}

if (profileForm) {
    loadProfile();
    profileForm.addEventListener('submit', saveProfile);
}

if (routineForm) {
    loadRoutineConfig();
    routineForm.addEventListener('submit', saveRoutineConfig);
}

if (streakButton) {
    loadStreaks();
    streakButton.addEventListener('click', registerStreak);
}

if (optionReminders || optionUpdates || optionSounds) {
    loadOptions();
    if (optionReminders) optionReminders.addEventListener('change', saveOptions);
    if (optionUpdates) optionUpdates.addEventListener('change', saveOptions);
    if (optionSounds) optionSounds.addEventListener('change', saveOptions);
}

const copyLink = async () => {
    const url = window.location.href;
    try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
            await navigator.clipboard.writeText(url);
            if (shareStatus) shareStatus.textContent = 'Enlace copiado al portapapeles.';
            return;
        }
    } catch (error) {
        console.warn('No se pudo usar clipboard API:', error);
    }

    const textArea = document.createElement('textarea');
    textArea.value = url;
    textArea.style.position = 'fixed';
    textArea.style.left = '-9999px';
    document.body.appendChild(textArea);
    textArea.select();

    try {
        document.execCommand('copy');
        if (shareStatus) shareStatus.textContent = 'Enlace copiado al portapapeles.';
    } catch (error) {
        if (shareStatus) {
            shareStatus.textContent = 'No se pudo copiar automáticamente. Usa el enlace manualmente.';
        }
        window.prompt('Copia este enlace:', url);
    }

    document.body.removeChild(textArea);
};

const sharePage = async () => {
    const url = window.location.href;
    if (navigator.share) {
        try {
            await navigator.share({ title: document.title, text: 'Mira esta página de HealthFit', url });
            if (shareStatus) shareStatus.textContent = 'Página compartida correctamente.';
            return;
        } catch (error) {
            console.warn('Compartir no funcionó:', error);
            if (shareStatus) shareStatus.textContent = 'No se pudo compartir directamente. Usa el botón Copiar enlace.';
            return;
        }
    }

    if (shareStatus) shareStatus.textContent = 'Compartir no está disponible en este navegador. Usa el botón Copiar enlace.';
};

if (copyLinkButton) {
    copyLinkButton.addEventListener('click', async () => {
        await copyLink();
    });
}

if (shareButton) {
    shareButton.addEventListener('click', async () => {
        await sharePage();
    });
}

const videoButtons = document.querySelectorAll('.video-select');
const mainVideo = document.getElementById('main-video');
if (videoButtons.length && mainVideo) {
    videoButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const videoUrl = button.getAttribute('data-video');
            if (videoUrl) {
                mainVideo.src = videoUrl;
                videoButtons.forEach((btn) => btn.classList.remove('active'));
                button.classList.add('active');
            }
        });
    });
}

const detailButtons = document.querySelectorAll('.toggle-details');
if (detailButtons.length) {
    detailButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const card = button.closest('.workout-card');
            const details = card ? card.querySelector('.routine-details') : null;
            if (details) {
                details.classList.toggle('hidden');
                button.textContent = details.classList.contains('hidden') ? 'Mostrar ejercicios' : 'Ocultar ejercicios';
            }
        });
    });
}

const anchorLinks = document.querySelectorAll('a[href^="#"]');
anchorLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
        event.preventDefault();
        const target = document.querySelector(link.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});
