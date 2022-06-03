FROM jupyter/base-notebook:python-3.8.8
WORKDIR "/home/jupyter"
USER root


RUN apt-get update && apt-get install -yq --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


RUN fix-permissions "/opt/" && \
    fix-permissions "/home/jupyter" && \
    fix-permissions "/home/${NB_USER}" 
    

ADD jupyter_notebook_config.py jupyter_server_config.py  /etc/jupyter/

ENV JUPYTER_ENABLE_LAB=yes
ENV GRANT_SUDO=yes

EXPOSE 8080

