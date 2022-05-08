import json
import sys
import time
from multiprocessing import Process

import zmq


def external_server(ip, port):
    """ Subscribe to list of topics and wait for messages. """

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://127.0.0.1:{port}")
    print(f"Bound server {port}")

    try:
        while True:
            message = socket.recv_json()
            print("Received message: ", message)
            if message["type"] == "status":
                socket.send_json({"role": "anything", "term": 0})
            else:
                socket.send_json({"i have no idea": False})
            time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit()


def start_external_server(ip, port):
    name = "client"
    Process(target=external_server, name=name, args=(ip, port)).start()

    # Sleep until killed
    while True:
        time.sleep(1)


if __name__ == "__main__":
    _this_file_name, config_path, node_id = sys.argv
    node_id = int(node_id)

    config_json = json.load(open(config_path))
    node_config = config_json["addresses"][node_id]
    ip, port = node_config["ip"], node_config["port"]
    start_external_server(ip, port)
