# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости с правами суперпользователя
RUN --mount=type=cache,sharing=locked,target=/root/.cache \
    pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска
CMD ["python", "main.py"]
RUN apt-get update && \ apt-get install -y build-essential libssl-dev
