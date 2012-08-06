postgresql:
    pkg:
        - installed
    service:
        - running
        - require:
            - pkg: postgresql

python-psycopg2:
    pkg:
        - installed
        - require:
            - pkg: postgresql

pebble_db_user:
    postgres_user.present:
        - name: pebble
        - runas: postgres
        - password: pebble
        - createdb: True
        - require:
            - pkg: python-psycopg2

mypebble_db:
    postgres_database.present:
        - name: mypebble_cms
        - runas: postgres
        - encoding: UTF8
        - owner: pebble
        - template: template0
        - require:
            - pkg: python-psycopg2
            - postgres_user: pebble_db_user
