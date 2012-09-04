www_user:
    user.present:
        - name: www
        - home: /home/www
        - shell: /bin/bash
