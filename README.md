# 🏆 Mundial 2026 — Pronosticador

App web 100% frontend (HTML/JS puro) para pronosticar los **104 partidos** del Mundial 2026.
Corre en cualquier navegador, sin backend para la UI — solo se necesita el servidor Python
para persistencia de datos.

---

## 🌐 App online

**http://194.34.232.193:8081/**

Servido por **nginx** + **server.py** via Docker Compose.

---

## ✨ Funcionalidades

| Feature | Detalle |
|---------|---------|
| **104 partidos** | Fase grupos (12×6) + R32 → R16 → QF → SF → 3° → Final |
| **Pronósticos** | Marcador local/visitante para cada partido |
| **Resultados reales** | Carga automática desde API oficial FIFA |
| **Estadísticas** | Pronosticados, aciertos 🟢, fallos 🔴, % precisión |
| **Modelo Panmure** | Predicciones y % de clasificación por grupo |
| **Filtros** | Por fase, por grupo |
| **Persistencia** | Auto-sync al servidor + Export/Import JSON |
| **Knockout dinámico** | Renombrar equipos en fases finales |

---

## 🗺️ Mundial 2026

- **48 equipos**, 12 grupos (A–L), 104 partidos
- **Sedes**: Canadá, México, EE.UU. — 16 estadios
- **Fechas**: 11 Jun – 19 Jul 2026

---

## 📁 Estructura del proyecto

```
worldcup-predictor/
├── index.html            # Frontend (todo en un HTML)
├── server.py             # API de persistencia (Python)
├── data/
│   └── predictions.json  # Datos guardados
├── deploy/
│   ├── docker-compose.yml
│   ├── Dockerfile.server
│   └── nginx.conf
├── .gitignore
├── LICENSE               # MIT
└── README.md
```

### index.html

App standalone de 730 líneas. Contiene:

- **UI**: partidos, inputs, tabs, estadísticas
- **🤖 Fetch Resultados FIFA** — usa `api.fifa.com/api/v3/calendar/matches` (gratis, sin key)
  con mapeo de nombres (Korea Republic → South Korea, USA → United States, etc.)
- **Auto-sync**: cada cambio se guarda al servidor (throttle 500ms)
- **💾 Sync Save / 📥 Sync Load** — conecta con `server.py` en puerto 8082

### server.py (Python)

Mini REST API para persistencia. Sin dependencias externas.

- `GET  /predictions.json` → descargar datos
- `POST /save-predictions` → guardar datos
- Puerto configurable via `WCUP_PORT` (default: 8082)
- Archivo configurable via `WCUP_DATA_FILE`

---

## 🐳 Despliegue local

```bash
cd worldcup-predictor/deploy
docker compose up -d
# App → http://localhost:8081
# API → http://localhost:8082
```

### Sin Docker (desarrollo)

```bash
# Servir HTML con cualquier HTTP server
# Ejemplo con Python:
cd worldcup-predictor
python3 -m http.server 8081 &

# Servidor de persistencia aparte:
python3 server.py
```

---

## 📡 Fetch Resultados FIFA

Usa la **API oficial de FIFA** sin necesidad de key:

```
https://api.fifa.com/api/v3/calendar/matches?idCompetition=17&from=2026-06-01&to=2026-07-19
```

El botón **🤖 Fetch Resultados FIFA** en la app:
1. Consulta la API de FIFA
2. Mapea nombres de equipos (USA → United States, Korea Republic → South Korea, etc.)
3. Actualiza solo resultados que no hayas ingresado manualmente

---

## 🔧 Desarrollo

### Principios

- **Simple**: HTML/JS puro, sin frameworks, sin npm, sin build
- **Ordenado**: Una responsabilidad por archivo
- **Portable**: Corre en cualquier browser, cualquier OS

### Para modificar la app

1. Editá `index.html`
2. Copiá al deploy: `cp index.html /opt/wcup-predictor/index.html`
3. Refrescá el browser (nginx sirve archivos estáticos, sin restart)

---

## 📄 Licencia

MIT — hacé lo que quieras.