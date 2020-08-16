import logging
from cassandra.cluster import Cluster

log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

KEYSPACE = "images"
cluster = Cluster(
    contact_points=['127.0.0.1'],
    port=9042,
)
session = cluster.connect()


def operateKeySpace(option=0,
                    image_time=None,
                    image_name=None,
                    image_label=None):
    if option == 0:
        log.info("Creating keyspace...")
        try:
            session.execute("""
                CREATE KEYSPACE %s
                WITH replication = {
                        'class': 'SimpleStrategy',
                        'replication_factor': '1' }
                """ % KEYSPACE)

            log.info("setting keyspace...")
            session.set_keyspace(KEYSPACE)

            log.info("creating table...")
            session.execute("""
                CREATE TABLE images_info (
                    image_time text PRIMARY KEY,
                    image_name text,
                    image_label text,
                )
                """)

        except Exception as e:
            log.error("Unable to create keyspace")
            log.error(e)
    elif option == 1:
        session.set_keyspace(KEYSPACE)
        info = [image_time, image_name, image_label]
        session.execute(
            """
        INSERT INTO images_info (image_time, image_name, image_label)
        VALUES (%s, %s, %s)
        """, info)
    elif option == 2:
        session.set_keyspace(KEYSPACE)
        rows = session.execute('select * from Images_info')
        return rows
    else:
        cluster.shutdown()
        cluster.is_shutdown
