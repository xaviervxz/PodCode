import websocket
import time
import thread
import json

def on_message(ws,message):
    d = json.load(message)
    command = d['command']
    ###TODO: Define possible commands and handle actions accordingly

def on_error(ws, error):
    print error

def on_close(ws):
        print "closed"

if __name__ == "__main__":
    websocket.enableTrace(True)
    url = "" ###http url server for ground statiom
    ws = websocket.WebSocketApp(url,on_message,on_error,on_close)
    ws.run_forever()
    while True:
        cmd = raw_input("Press I to enter info or D to enter Danger or X to exit")
        if cmd == "I":
            info = raw_input("Press A for air quality, G for gps, P for pressure, S for Sonar, and T for temp")
            if info == "A":
                mydict = {}
                mydict['info'] = "air quality"
                status = raw_input("safe/caution/unsafe?")
                mydict['status'] = status
                location = raw_input("outside/inside?")
                mydict['location'] = location
                heavy_prescence = raw_input("Enter Symbol (e.g. C02) for present chemical, or none")
                mydict['heavy_prescence'] = heavy_prescence
                timestamp = time.strftime("%H:%M:%S") + time.strftime("%d/%m/%Y")
                mydict['timestamp'] = timestamp
                string = json.dumps(mydict)
                ws.send(string)
            elif info = "G":
                    
