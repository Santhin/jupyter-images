import os
import shutil

c = get_config()  # noqa: F821
c.NotebookApp.open_browser = False
c.ServerApp.token = ''
c.ServerApp.password = ''
c.ServerApp.base_url=os.getenv('NB_PREFIX', '')
c.ServerApp.root_dir = f"/home/jupyter"
c.ServerApp.notebook_dir = "/home/jupyter"

# https://github.com/jupyter/notebook/issues/3130
c.FileContentsManager.delete_to_trash = False
c.FileCheckpoints.checkpoint_dir = '/home/jovyan/checkpoints'

def _codeserver_command():
    full_path = shutil.which('code-server')
    if not full_path:
        raise FileNotFoundError('Can not find code-server in $PATH')
    working_dir = os.getenv("CODE_WORKINGDIR", None)
    if working_dir is None:
        working_dir = os.getenv("JUPYTER_SERVER_ROOT", ".")

    return [full_path, f'--port=7000', "--auth", "none", working_dir ]

c.ServerProxy.servers = {}
c.ServerProxy.servers['cloudbeaver'] = {
    'command': ['/bin/bash', '-c', 'cd /opt/cloudbeaver && ./run-server.sh', '{port}'],
    'port': 8978,
    'absolute_url': True,
    'timeout': 60,
    'new_browser_tab': False,
    'launcher_entry': {
        'title': "CloudBeaver",
        'icon_path': '/opt/logos/cloudbeaver.svg',
    }
}   
