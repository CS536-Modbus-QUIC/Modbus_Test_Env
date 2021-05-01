# Modbus Test Environment

We will test Modbus over QUIC and the original PyModbus in this environment.

## Setup the Virtual Network
```sh
$ cd <path-to-folder>

# Window 1
$ make controller

# Window 2
$ make mininet

# Window 3
$ make cli
# password: rocks
$ app activate fwd

# Window 4
$ make netcfg
$ make start-net
```

## Run the experiment
Modbus over QUIC
```sh
# Window 5
$ make host-h1
$ cd aioquic
$ python3 examples/modbus_server.py --certificate tests/ssl_cert.pem --private-key tests/ssl_key.pem --host 10.0.0.1 --port 502

# Window 6
$ make host-h2
$ cd aioquic
$ python3 examples/modbus_client.py --ca-certs tests/pycacert.pem --port 502 --host 10.0.0.1
```

Pymodbus TCP + TLS
```sh
# Window 5
$ make host-h1
$ cd pymodbus/examples/common
$ python3 asyncio_server.py

# Window 6
$ make host-h2
$ cd pymodbus/examples/common
$ python3 async_asyncio_client.py
```