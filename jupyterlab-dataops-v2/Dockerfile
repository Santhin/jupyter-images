FROM dbeaver/cloudbeaver:22.3.5 AS builder-dbeaver
FROM jupyter/base-notebook:python-3.9.12
ENV NB_USER=jovyan
ENV NB_UID=1000
ENV NB_GID=100
ENV CONDA_DIR=/opt/conda

USER root

RUN apt-get update && apt-get install -yq --no-install-recommends \
    curl \
    git \
    openjdk-11-jdk \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# code-server install
RUN curl -fsSL https://code-server.dev/install.sh | sh && \
    rm -rf "${HOME}/.cache"

# delete user jupyter,jovyan if exists
RUN  if [ "$( id $NB_USER 2>/dev/null | wc -l)" -eq 1 ]; then userdel $NB_USER; fi
RUN  if [ "$( id jovyan 2>/dev/null | wc -l)" -eq 1 ]; then userdel jovyan; fi
# add user $NB_USER if not exits
RUN  if [ "$( id $NB_USER 2>/dev/null | wc -l)" -eq 0 ]; then useradd -ms /bin/bash -u $NB_UID $NB_USER; fi
# add group GID 1001 if not exists (for Vertex)
RUN  if [ "$( grep 1001 /etc/group | wc -l)" -eq 0 ]; then groupadd -g 1001 jupyter-group; fi
# allow passwordless sudo and add group required by kubeflow
RUN echo "$NB_USER ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/notebook && \
    groupadd -g 1337 nbusers


COPY --from=builder-dbeaver /opt/cloudbeaver/ /opt/cloudbeaver/
COPY resources/logos/* /opt/logos/
RUN chmod 755 /opt/cloudbeaver/run-server.sh 
COPY resources/cloudbeaver/conf /opt/cloudbeaver/conf

USER $NB_USER

COPY requirements/ /opt/requirements/
RUN pip install -r /opt/requirements/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" 

COPY resources/jupyter/jupyter_notebook_config.py resources/jupyter/jupyter_server_config.py   /etc/jupyter/

COPY resources/vsc/vsix/ /opt/vsix/
RUN code-server --install-extension ms-python.python \
    code-server --install-extension /opt/vsix/innoverio.vscode-dbt-power-user-0.5.9.vsix \
    code-server --install-extension /opt/vsix/bastienboutonnet.vscode-dbt-0.5.1.vsix
COPY resources/vsc/settings.json "/home/${NB_USER}/.local/share/code-server/User/settings.json"
# Expose port for Vertex AI compatibility
ENV JUPYTER_ENABLE_LAB=yes
WORKDIR "/home/jupyter"
EXPOSE 8080