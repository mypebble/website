ssh_directory:
    file.directory:
        - name: /root/.ssh
        - user: root
        - group: root
        - mode: 700
        - makedirs: False

mercurial:
    ssh_known_hosts:
        - present
        - user: root
        - name: mercurial.talktopebble.co.uk
        - fingerprint: 43:8d:a3:25:46:d8:e3:72:00:45:86:94:ca:de:a7:78
        - config: /root/.ssh/known_hosts
        - require:
            - file: ssh_directory

mypebble:
    hg.latest:
        - name: ssh://hg@mercurial.talktopebble.co.uk/mypebble
        - target: /home/www/mypebble
        - require:
            - user: www
            - ssh_known_hosts: mercurial

mypebble_perm:
    file.directory:
        - name: /home/www/mypebble
        - user: www
        - group: www
        - mode: 755
        - recurse:
            - user
            - group
        - require:
            - hg: mypebble

hg_perm:
    file.directory:
        - name: /home/www/mypebble/.hg
        - user: root
        - group: root
        - mode: 755
        - recurse:
            - user
            - group
        - require:
            - mypebble_perm

python-virtualenv:
    pkg:
        - installed

venv:
    virtualenv.managed:
        - name: /home/www/mypebble
        - requirements: /home/www/mypebble/requirements
        - require:
            - file: mypebble_perm
            - pkg: python-virtualenv
