FROM jupyter/base-notebook:python-3.8.8
USER root


RUN apt-get update && apt-get install -yq --no-install-recommends \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# code-server install
RUN curl -fsSL https://code-server.dev/install.sh | sh && \
    rm -rf "${HOME}/.cache"

COPY resources/vsc/vsix/ /opt/vsix/
RUN code-server --install-extension ms-python.python \
    code-server --install-extension /opt/vsix/innoverio.vscode-dbt-power-user-0.5.9.vsix \
    code-server --install-extension /opt/vsix/bastienboutonnet.vscode-dbt-0.5.1.vsix
COPY resources/vsc/settings.json "/home/jupyter/.local/share/code-server/User/settings.json"
RUN pip install jupyter-server-proxy && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" 

ADD jupyter_notebook_config.py jupyter_server_config.py  /etc/jupyter/

ENV JUPYTER_ENABLE_LAB=yes
WORKDIR "/home/jupyter"
EXPOSE 8080
COPY resources/logos/* /opt/logos/


