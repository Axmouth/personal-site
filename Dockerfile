FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Define working directory
RUN mkdir /code
WORKDIR /code

# Copy files and install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/

# ENV DJANGO_DEBUG True
ARG DJANGO_DEBUG=False
WORKDIR /code/mybiosite
RUN python manage.py collectstatic --noinput

# RUN python /code/mybiosite/manage.py migrate

# Set the running environment as production
# ENV NODE_ENV production
# ENV POSTGRES_HOST host.docker.internal

# Expose on specified network port
EXPOSE 8000

# Executing defaults
# CMD ["pm2-docker", "start", "process.json"]