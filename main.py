import os
import random
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# --- CONFIGURATION ---
OWNER_NAME = "AFFAN MARK"
TOOL_NAME = "ULTRA HEAVY CLONER"
FIXED_PASSWORD = "AFFANMARK376"

# --- DATA LIST ---
MY_OLD_IDS = [
    "100001969555649|12345678", "100001241816244|123456789", "100001474307734|123456789",
    "100001231429391|123456", "100001420901985|123456", "100001499197000|123456789",
    "100001236273909|123456", "100001500570887|123456789", "100001254576308|123456",
    "100001188137040|123456", "100001306141710|123456", "100001875667664|1234567"
]

def generate_heavy_cookie():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    datr = "".join(random.choice(chars) for _ in range(24))
    sb = "".join(random.choice(chars) for _ in range(24))
    fake_uid = "6158" + str(random.randint(1111111111, 9999999999))
    xs_val = f"{random.randint(40, 50)}%3A{''.join(random.choice(chars) for _ in range(14))}%3A2%3A{random.randint(1770000000, 1780000000)}"
    return f"datr={datr};sb={sb};c_user={fake_uid};xs={xs_val};"

# --- HTML UI ---
HTML_UI = f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{OWNER_NAME} TOOL</title>
    <style>
        body {{ background: #000; color: #0f0; font-family: monospace; text-align: center; padding: 10px; }}
        .header {{ border: 1px solid #0f0; padding: 10px; margin-bottom: 20px; font-size: 12px; white-space: pre; }}
        .form-box {{ border: 1px solid #fff; padding: 20px; max-width: 400px; margin: auto; }}
        input, select, button {{ width: 100%; padding: 12px; margin: 10px 0; background: #000; color: #0f0; border: 1px solid #0f0; box-sizing: border-box; }}
        button {{ background: #0f0; color: #000; font-weight: bold; cursor: pointer; }}
        .result-item {{ border-bottom: 1px dashed #0f0; padding: 10px; text-align: left; font-size: 12px; margin-top: 10px; }}
    </style>
</head>
<body>
    <div class="header">
  █████  ██   ██ ███    ██ 
 ██   ██ ██   ██ ████   ██ 
 ███████ ██   ██ ██ ██  ██ 
 ██   ██  ██ ██  ██  ██ ██ 
 ██   ██   ███   ██   ████ 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 AUTHOR : {OWNER_NAME}
 TOOL   : {TOOL_NAME}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    </div>

    <div class="form-box">
        <input type="password" id="pass" placeholder="ENTER PASSWORD">
        <select id="method">
            <option value="MIXED">METHOD MIXED</option>
            <option value="2009">METHOD 2009</option>
            <option value="2010">METHOD 2010</option>
        </select>
        <button onclick="runTool()">START CLONING</button>
    </div>

    <div id="logs"></div>

    <script>
        function runTool() {{
            const p = document.getElementById('pass').value;
            const m = document.getElementById('method').value;
            const logBox = document.getElementById('logs');

            if(p !== "{FIXED_PASSWORD}") {{ alert("Wrong Password!"); return; }}

            logBox.innerHTML = "<p style='color:yellow'>[*] Extracting IDs...</p>" + logBox.innerHTML;

            fetch('/api/crack', {{
                method: 'POST',
                headers: {{'Content-Type': 'application/x-www-form-urlencoded'}},
                body: `method=${{m}}`
            }})
            .then(res => res.json())
            .then(data => {{
                let html = `
                    <div class="result-item">
                        <span style="color:#0f0">[AVN-OK]</span> ${{data.id_data}}<br>
                        <span style="color:yellow">YEAR:</span> ${{data.year}}<br>
                        <span style="color:#fff">COOKIE:</span> ${{data.cookie}}
                    </div>
                `;
                logBox.innerHTML = html + logBox.innerHTML;
            }});
        }}
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_UI)

@app.route('/api/crack', methods=['POST'])
def crack_api():
    method = request.form.get('method')
    id_data = random.choice(MY_OLD_IDS)
    year = method if method != "MIXED" else random.choice(["2009", "2010", "2011"])
    cookie = generate_heavy_cookie()
    return jsonify({{"id_data": id_data, "year": year, "cookie": cookie}})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
