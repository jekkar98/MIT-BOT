# Используем более стабильную версию Python
FROM python:3.10-slim

WORKDIR /app

# Устанавливаем только необходимые пакеты
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev

# Добавляем Rust и Cargo
RUN apt-get install -y cargo rustc

# Создаем директорию для кэша
RUN mkdir /tmp/cargo && \
    chmod 777 /tmp/cargo

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

# Настраиваем права доступа
RUN chown -R deploy:deploy /home/deploy/app

CMD ["python", "main.py"]
