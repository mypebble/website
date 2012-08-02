nginx:
    pkg:
        - installed
    service:
        - running
        - require:
            - pkg: nginx

available:
    file:
        - name: /etc/nginx/sites-available/mypebble.co.uk
        - managed
        - source: salt://nginx.conf
        - require:
            - pkg: nginx

enabled:
    file:
        - name: /etc/nginx/sites-enabled/mypebble.co.uk
        - managed
        - source: salt://nginx.conf
        - require:
            - pkg: nginx
