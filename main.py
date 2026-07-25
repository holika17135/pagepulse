from flask import Flask, render_template_string, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string('''<!DOCTYPE html>
<html><body style="padding:40px;font-family:Arial">
<h1>PagePulse SEO Audit</h1>
<input id="url" value="https://google.com" style="width:300px;padding:10px">
<button onclick="audit()">Audit Chey</button>
<pre id="out" style="background:#eee;padding:20px"></pre>
<script>
async function audit(){
 let r = await fetch('/api/audit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({url:document.getElementById('url').value})});
 document.getElementById('out').innerText = JSON.stringify(await r.json(),null,2);
}
</script></body></html>''')

@app.route("/api/audit", methods=["POST"])
def audit():
    url = request.json["url"]
    res = requests.get(url, timeout=10)
    soup = BeautifulSoup(res.text, 'html.parser')
    return jsonify({"status": res.status_code, "title": soup.title.string if soup.title else "Ledu"})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)