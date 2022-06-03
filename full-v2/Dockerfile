FROM dbeaver/cloudbeaver:22.0.5 AS builder-dbeaver
FROM jupyter/base-notebook:python-3.8.8
USER root
WORKDIR "/home/jupyter"

RUN apt-get update && apt-get install -yq --no-install-recommends \
    curl \
    git \
    openjdk-11-jdk \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# code-server install
RUN curl -fsSL https://code-server.dev/install.sh | sh && \
    rm -rf "${HOME}/.cache"

COPY resources/vsc/vsix/ /opt/vsix/
RUN code-server --install-extension ms-python.python \
    code-server --install-extension /opt/vsix/innoverio.vscode-dbt-power-user-0.5.9.vsix \
    code-server --install-extension /opt/vsix/bastienboutonnet.vscode-dbt-0.5.1.vsix

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


