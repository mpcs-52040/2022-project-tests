import json
import sys
import time
from multiprocessing import Process
from typing import Dict

import zmq


def to_json_str(message: Dict):
    return json.dumps(message)


def from_json_str(message: str):
    return json.loads(message)


def send_json(socket, message: Dict):
    socket.send_json(to_json_str(message))


def recv_json(socket):
    return from_json_str(socket.recv_json())


def external_server(ip, port):
    """ Subscribe to list of topics and wait for messages. """

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://127.0.0.1:{port}")
    print(f"Bound server {port}")

    try:
        while True:
            message = recv_json(socket)
            # print("Received message: ", message)
            if message["type"] == "status":
                send_json(socket, {"role": "anything", "term": 0})
            else:
                send_json(socket, {"i have no idea": False})
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
