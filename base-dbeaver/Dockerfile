FROM dbeaver/cloudbeaver:22.0.5 AS builder-dbeaver
FROM jupyter/base-notebook:python-3.8.8
USER root
WORKDIR "/home/jupyter"

RUN apt-get update && apt-get install -yq --no-install-recommends \
    curl \
    git \
    openjdk-11-jdk \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder-dbeaver /opt/cloudbeaver/ /opt/cloudbeaver/
COPY resources/logos/* /opt/logos/
RUN chmod 755 /opt/cloudbeaver/run-server.sh 
COPY resources/cloudbeaver/conf /opt/cloudbeaver/conf
COPY resources/logos/* /opt/logos/

RUN pip install jupyter-server-proxy && \
    fix-permissions "/opt/" && \
    fix-permissions "/home/jupyter" && \
    fix-permissions "/home/${NB_USER}" 

ADD jupyter_notebook_config.py jupyter_server_config.py  /etc/jupyter/

ENV JUPYTER_ENABLE_LAB=yes

EXPOSE 8080


