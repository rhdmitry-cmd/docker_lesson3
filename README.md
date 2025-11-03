# Docker Lesson 3

Небольшой пример Python-приложения, упакованного в Docker.

## Состав
- `main.py` — простой скрипт Python
- `requirements.txt` — зависимости
- `Dockerfile` — сборка Docker-образа

## Запуск локально
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: . .venv/Scripts/Activate.ps1
pip install -r requirements.txt
python main.py
```

## Сборка и запуск в Docker
```bash
# Сборка образа
docker build -t docker-lesson3:latest .

# Запуск контейнера
docker run --rm docker-lesson3:latest
```

## Полезно
- Удалённый репозиторий: `https://github.com/rhdmitry-cmd/docker_lesson3.git`


