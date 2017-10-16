import json
from http.server import *


def processImage(str_img):
    return str_img

class GetHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        print("post received!")
        
        try:
            
            if self.path.endswith("/process"):

                content_len = int(self.headers['Content-Length'])
                post_body = self.rfile.read(content_len)

                data = str(post_body.decode('utf-8'))
                json_data = json.loads(data)
                str_img = json_data["img"]

                result = processImage(str_img)
                print("process result:", result)



                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                #self.send_header("Access-Control-Expose-Headers", "Access-Control-Allow-Origin")
                self.end_headers()

                json_response = json.dumps({"answer": "post recibido!!"});
                self.wfile.write(bytes(json_response, 'utf-8'))

                print("respuesta enviada")

        except Exception as e:
            print("[ERROR]" + str(e))

        return


if __name__ == "__main__":
    HandlerClass = GetHandler
    ServerClass = HTTPServer

    protocol = "HTTP/1.0"
    host = "0.0.0.0"
    port = 5050

    server_address = (host, port)

    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)
    print ('Starting server at http://0.0.0.0:5050')

    httpd.serve_forever()