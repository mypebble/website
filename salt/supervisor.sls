supervisor:
    pkg:
        - installed
    service:
        - running
        - require:
            - pkg: supervisor

/etc/supervisor/conf.d/mypebble.conf:
    file:
        - managed
        - source: salt://supervisor.conf
        - require:
            - pkg: supervisor
