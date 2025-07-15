FROM python:3.11-slim

# Создаем временного пользователя
RUN useradd -m deploy
USER deploy

WORKDIR /home/deploy/app

# Устанавливаем необходимые пакеты
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev cargo rustc

# Создаем директорию для кэша cargo
RUN mkdir /home/deploy/.cargo && \
    chmod 755 /home/deploy/.cargo

# Копируем файлы проекта
COPY --chown=deploy:deploy . /home/deploy/app

# Устанавливаем зависимости от имени пользователя
RUN pip install --no-cache-dir -r requirements.txt

# Возвращаемся к root для настройки прав
USER root

# Настраиваем права доступа
RUN chown -R deploy:deploy /home/deploy/app

CMD ["python", "main.py"]
