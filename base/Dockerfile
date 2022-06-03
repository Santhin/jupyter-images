FROM jupyter/base-notebook:python-3.8.8
USER root


RUN apt-get update && apt-get install -yq --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


ADD jupyter_notebook_config.py jupyter_server_config.py  /etc/jupyter/

ENV JUPYTER_ENABLE_LAB=yes
WORKDIR "/home/jupyter"
EXPOSE 8080


