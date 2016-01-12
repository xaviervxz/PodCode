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
            mydict = {}
            if info == "A":
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
                mydict['info'] = "gps"
                latitude = double(raw_input("enter latitude"))
                longitude = double(raw_input("enter longitude"))
                mydict['latitude'] = latitude
                mydict['longitude'] = longitude
                status = raw_input("pre-start/en route/post-stop?")
                mydict['status'] = status
                timestamp = time.strftime("%H:%M:%S") + time.strftime("%d/%m/%Y")
                mydict['timestamp'] = timestamp
                string = json.dumps(mydict)
                ws.send(string)
            elif info = "P":
                mydict['info'] = "pressure"
                measurement = double(raw_input("enter measurement"))
                mydict['measurement'] = measurement
                location = raw_input("outside/inside?")
                mydict['location'] = location
                timestamp = time.strftime("%H:%M:%S") + time.strftime("%d/%m/%Y")
                mydict['timestamp'] = timestamp
                string = json.dumps(mydict)
                ws.send(string)
            elif info = "S":
                mydict['info'] = "sonar"
                dft = double(raw_input("enter estimated distance from tube"))
                quadrant = raw_input("1/2/3/4?")
                mydict['est_dist_from_tube'] = dft
                mydict['quadrant'] = quadrant
                status = raw_input("safe/caution/unsafe")
                mydict['status'] = status
                timestamp = time.strftime("%H:%M:%S") + time.strftime("%d/%m/%Y")
                mydict['timestamp'] = timestamp
                string = json.dumps(mydict)
                ws.send(string)
            elif info = "T":
                mydict['info'] = "temperatrue"
                farenheit = raw_input("enter degrees in farenheit")
                celsius = raw_input("enter degrees in celsius")
                mydict['farenheit'] = farenheit
                mydict['celsius'] = celsius
                location = raw_input("outside/inside?")
                mydict['location'] = location
                timestamp = time.strftime("%H:%M:%S") + time.strftime("%d/%m/%Y")
                mydict['timestamp'] = timestamp
                status = raw_input("safe/caution/unsafe")
                mydict['status'] = status
                string = json.dumps(mydict)
                ws.send(string)
            else:
                print "Wrong Key"
        elif cmd == "D":
            mydict = {}
            risk = raw_input("HIGH/MED/LOW?")
            mydict['risk'] = risk
            issue = raw_input("what's the issue?")
            mydict['issue'] = issue
            solution = raw_input("what's the solution?")
            mydict['solution'] = solution
            info_type = raw_input("any more info?")
            mydict['info_type'] = info_type
            timestamp = time.strftime("%H:%M:%S") + time.strftime("%d/%m/%Y")
            mydict['timestamp'] = timestamp
            string = json.dumps(mydict)
            ws.send(string)
        elif cmd == "X":
            break
        else:
            print "Wrong Key"
