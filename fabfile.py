from fabric.api import env, local, run, sudo

from fabric.decorators import task

from fabric.contrib import django

from fabric.colors import green

django.settings_module('mypebble.settings')

target_hosts = {
    'testing': 'test',
}


def info(msg):
    print green(msg)


@task
def install():
    """Install and configure the management systems to allow for deployment.
    """

    info('Installing Salt')
    frontend = 'DEBIAN_FRONTEND=noninteraction'
    salt_ppa = 'ppa:saltstack/salt'
    salt_packages = ['salt-master', 'salt-minion']


    sudo(
        '{frontend} apt-get install '
        'python-software-properties'.format(frontend=frontend)
    )
    sudo('add-apt-repository {ppa}'.format(ppa=salt_ppa))
    sudo('{frontend} apt-get update'.format(frontend=frontend))

    sudo('{frontend} apt-get install {packages}'.format(
        frontend=frontend,
        packages=' '.join(salt_packages),
    ))
