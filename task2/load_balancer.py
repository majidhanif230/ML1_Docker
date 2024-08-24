from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Use Docker service names instead of localhost
servers = ["http://backend1:5000", "http://backend2:5001"]
current = 0

def get_next_server():
    global current
    server = servers[current]
    current = (current + 1) % len(servers)
    return server

@app.route('/', methods=['GET', 'POST'])
def load_balancer():
    server = get_next_server()
    try:
        if request.method == 'POST':
            resp = requests.post(server, data=request.data)
        else:
            resp = requests.get(server, params=request.args)
        return Response(resp.content, status=resp.status_code)
    except requests.exceptions.RequestException as e:
        return Response(f"Error forwarding request to backend server: {e}", status=500)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
