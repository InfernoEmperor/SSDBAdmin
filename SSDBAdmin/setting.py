import os

DB_CONFIG = [{
    "host": "10.10.0.23",
    "port": "12001"
}, {
    "host": "10.10.0.23",
    "port": "12000"
}, {
    "host": "10.10.0.23",
    "port": "12002"
}, {
    "host": "10.10.0.23",
    "port": "12003"
}, {
    "host": "10.10.0.23",
    "port": "12200"
}, {
    "host": "10.10.0.22",
    "port": "14200"
}, {
    "host": "192.168.6.208",
    "port": "14200"
}]

SERVICE_CONFIG = {"host": "127.0.0.1", "port": "9999", "debug": False}

ENSURE_ASCII = False

VERSION = '3.0.0'

# ------ get config by env(in Docker) ----

db_config = os.getenv("DB_CONFIG", "")  # 127.0.0.1:8888,127.0.0.1:8080
if db_config:
    try:
        DB_CONFIG = [{
            "host": _.split(":")[0],
            "port": _.split(":")[1]
        } for _ in db_config.split(',')]
    except Exception:
        pass

server_host = os.getenv("SERVER_HOST", "")
if server_host:
    SERVICE_CONFIG["host"] = server_host

server_port = os.getenv("SERVER_PORT", "")
if server_port:
    SERVICE_CONFIG["port"] = server_port
