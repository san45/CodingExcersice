import websocket
import thread
import time
import json

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

str='{"event":"subscribe","streams":["ethinr@trades"]}'

def on_open(ws):
    def run(*args):
        time.sleep(2)
        ws.send(str)
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.wazirx.com/stream",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever():

    
