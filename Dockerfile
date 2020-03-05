FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Define working directory
RUN mkdir /code
WORKDIR /code

# Copy files and install dependencies
COPY stable-req.txt /code/
RUN pip install --no-cache-dir -r stable-req.txt
COPY . /code/

# ENV DJANGO_DEBUG True
ARG DJANGO_DEBUG=False
WORKDIR /code/mybiosite
RUN python manage.py collectstatic --noinput

# RUN python /code/mybiosite/manage.py migrate

# Set the running environment as production

# Expose on specified network port
EXPOSE 8000

# Executing defaults