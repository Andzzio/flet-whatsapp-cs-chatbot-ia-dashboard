# 🤖 BOTY Dashboard

Dashboard de administración para bot django de mi otro repositorio.

## ✨ Características

- 💬 Visualización de conversaciones en tiempo real
- 🔄 Sincronización automática con el servidor
- 🤖 Control manual del bot por contacto
- 📤 Envío de mensajes directos desde el dashboard
- 🔐 Autenticación segura por token

## 📥 Instalación

### Opción 1: Ejecutable (Recomendado para clientes)

1. Ve a la sección [Releases](../../releases)
2. Descarga el ejecutable para tu sistema operativo:
   - `BOTY-Dashboard-Linux` para Linux
   - `BOTY-Dashboard-Windows.exe` para Windows
   - `BOTY-Dashboard-macOS` para macOS
3. Ejecuta el archivo descargado

### Opción 2: Desde código (Para desarrolladores)

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/flet-whatsapp-cs-chatbot-ia-dashboard.git
cd flet-whatsapp-cs-chatbot-ia-dashboard

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
flet run src/main.py
```

## ⚙️ Configuración Inicial

1. **Primera ejecución:** Al abrir el dashboard por primera vez, verás la pantalla de ajustes
2. **Token de API:**
   - Haz clic en el ícono de ajustes (⚙️)
   - Ingresa tu token de autenticación en el campo proporcionado
   - Presiona Enter para guardar
3. **Conectar:** El dashboard se sincronizará automáticamente con el servidor

## 🎮 Uso

### Vista de Chat

- **Seleccionar contacto:** Haz clic en un contacto del sidebar
- **Enviar mensaje:** Escribe en el campo de texto y presiona Enter
- **Control del bot:**
  - Switch (OFF) = Bot automático activo
  - Switch (ON) = Modo manual activado

### Control Manual del Bot

Cuando activas el modo manual (switch rojo):

- El bot NO responderá automáticamente a ese contacto
- Podrás responder manualmente desde el dashboard
- Los mensajes del usuario se guardan normalmente
- Al desactivar el modo manual, el bot solo responderá a mensajes nuevos

## 🔧 Tecnologías

- **Frontend:** [Flet](https://flet.dev/) - Framework Python para UI
- **Backend:** Django REST API
- **Sincronización:** Polling cada 5 segundos
- **Persistencia:** JSON local + Base de datos remota

## 📋 Requisitos del Sistema

- **Sistema Operativo:** Linux, Windows 10+, macOS 10.14+
- **RAM:** Mínimo 512 MB
- **Espacio en disco:** 50 MB
- **Conexión a internet:** Requerida

## 🛠️ Desarrollo

### Crear ejecutable

```bash
# Para Linux
flet build linux

# Para Windows
flet build windows

# Para macOS
flet build macos
```

El ejecutable se generará en `build/[plataforma]/`

## 📞 Soporte

Para reportar problemas o solicitar funcionalidades:

- Abre un [Issue](../../issues)
- Email: tu-email@ejemplo.com

## 📄 Licencia

Este proyecto es privado y de uso exclusivo para clientes autorizados.

---

**Desarrollado por Andzzio**
