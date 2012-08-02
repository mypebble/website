www_group:
    group.present:
        - name: www
        - system: False

www_user:
    user.present:
        - name: www
        - shell: /bin/bash
        - home: /home/www
        - groups:
            - www
        - require:
            - group: www_group
