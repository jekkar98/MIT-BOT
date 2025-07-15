# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем необходимые системные библиотеки
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev cargo rustc

# Создаем временный каталог с правильными правами
RUN mkdir /tmp/cargo && \
    chmod 777 /tmp/cargo

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN --mount=type=cache,sharing=locked,target=/root/.cache \
    pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска
CMD ["python", "main.py"]
