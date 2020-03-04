FROM postgres:12

COPY ./postgres/init/01-db_setup.sh /docker-entrypoint-initdb.d/01-db-setup.sh
RUN chmod u+x /docker-entrypoint-initdb.d/01-db-setup.sh
# RUN bash /docker-entrypoint-initdb.d/01-db-setup.sh
# RUN bash /docker-entrypoint-initdb.d/01-db-setup.sh

# Expose on specified network port
EXPOSE 5432