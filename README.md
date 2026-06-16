# World Cup 2026 Predictor

Pronosticador de los 104 partidos del Mundial 2026.
Frontend HTML/JS + Python API para persistencia.
Desplegado con Docker Swarm en puerto **8081**.

## Estructura

```
worldcup-predictor/
├── index.html              ← Frontend (app principal)
├── server.py               ← API REST (persistencia pronósticos)
├── data/
│   └── predictions.json    ← Datos guardados
├── deploy/
│   ├── docker-compose.yml
│   ├── Dockerfile.server
│   └── nginx.conf
├── Makefile                ← setup, sync, status
├── sync.sh                 ← git pull/commit/push
└── .gitignore
```

## Comandos

```bash
make sync     # Backup a GitHub
make status   # Ver estado del repo
```

## URLs

- Frontend: http://<host>:8081
- API: http://<host>:8082

## Docker

El servicio se despliega con Docker Swarm:

```bash
docker service update --image nginx:alpine wcup_predictor
```

O usando docker-compose desde deploy/:
```bash
cd deploy && docker stack deploy -c docker-compose.yml wcup
```
