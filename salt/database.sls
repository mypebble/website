postgres:
    pkg:
        - installed
    service:
        - running
        - require:
            - pkg: postgresql

psycopg2:
    pkg:
        - installed

pebble_db_user:
    postgres_user.present:
        - name: pebble
        - password: pebble
        - require:
            - pkg:
                - postgres
                - psycopg2

mypebble_db:
    postgres_database.present:
        - name: mypebble
        - encoding: UTF8
        - owner: pebble
        - template: template0
        - require:
            - pkg:
                - postgres
                - psycopg2
