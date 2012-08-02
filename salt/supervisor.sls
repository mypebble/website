supervisor:
    pkg:
        - installed
    service:
        - running
        - require:
            - pkg: supervisor
            - user: www_user

/etc/supervisor/conf.d/mypebble.conf:
    file:
        - managed
        - source: salt://supervisor.conf
        - require:
            - pkg: supervisor
