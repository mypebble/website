pebble_db_user:
    postgres_user.present:
        - name: pebble
        - password: pebble

mypebble_db:
    postgres_database.present:
        - name: mypebble
        - encoding: UTF8
        - owner: pebble
        - template: template0
