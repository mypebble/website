nginx:
    pkg:
        - installed
    service:
        - running
        - require:
            - pkg: nginx
            - file: /srv/www/mypebble
            - user: www_user

available:
    file:
        - name: /etc/nginx/sites-available/mypebble.co.uk
        - managed
        - source: salt://nginx.conf
        - require:
            - pkg: nginx
            - user: www_user

enabled:
    file:
        - name: /etc/nginx/sites-enabled/mypebble.co.uk
        - managed
        - source: salt://nginx.conf
        - require:
            - pkg: nginx
            - user: www_user

/srv/www/talktopebble/log:
    file.directory:
        - user: www
        - group: www
        - mode: 755
        - makedirs: True
        - require:
            - pkg: nginx
            - user: www_user

/srv/www/schoolfund/log:
    file.directory:
        - user: www
        - group: www
        - mode: 755
        - makedirs: True
        - require:
            - pkg: nginx
            - user: www_user

/srv/www/mypebble:
    file.symlink:
        - target: /home/www/mypebble
        - require:
            - user: www_user

/srv/www/mypebble/log:
    file.directory:
        - user: www
        - group: www
        - mode: 755
        - require:
            - file: /srv/www/mypebble
            - user: www_user
