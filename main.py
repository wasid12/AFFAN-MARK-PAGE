import os
import random
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# --- CONFIGURATION ---
OWNER_NAME = "AFFAN MARK"
TOOL_NAME = "ULTRA HEAVY CLONER"
FIXED_PASSWORD = "AFFANMARK376"

# Background Image URL (Jo tumne di thi)
BG_IMAGE = "https://images.clothes.com/1000086890.jpg" 

# --- DATA LIST ---
MY_OLD_IDS = [
    "100001969555649|12345678", "100001241816244|123456789", "100001474307734|123456789",
    "100001231429391|123456", "100001420901985|123456", "100001499197000|123456789",
    "100001236273909|123456", "100001500570887|123456789", "100001254576308|123456"
]

# --- HTML UI ---
HTML_UI = f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{OWNER_NAME} TOOL</title>
    <style>
        body {{ 
            background: url('{BG_IMAGE}') no-repeat center center fixed; 
            background-size: cover;
            color: #0f0; 
            font-family: monospace; 
            text-align: center; 
            padding: 10px;
            margin: 0;
        }}
        .overlay {{ background: rgba(0, 0, 0, 0.7); min-height: 100vh; padding: 20px 10px; }}
        .header {{ border: 1px solid #0f0; padding: 15px; margin-bottom: 20px; font-size: 14px; background: rgba(0,0,0,0.8); }}
        .banner-text {{ font-size: 30px; font-weight: bold; color: #0f0; margin-bottom: 5px; letter-spacing: 5px; }}
        .form-box {{ border: 1px solid #fff; padding: 15px; max-width: 450px; margin: auto; background: rgba(0,0,0,0.9); }}
        
        input {{ width: 100%; padding: 12px; margin-bottom: 15px; background: #000; color: #0f0; border: 1px solid #0f0; box-sizing: border-box; }}
        
        .method-row {{ display: flex; align-items: center; justify-content: space-between; border: 1px solid #444; margin-bottom: 8px; background: #000; }}
        .method-name {{ padding: 10px; font-size: 13px; color: #0f0; text-align: left; flex: 1; }}
        .btn-next {{ background: #0f0; color: #000; border: none; padding: 10px 20px; font-weight: bold; cursor: pointer; min-width: 80px; }}
        .btn-exit {{ background: #f00; color: #fff; border: none; padding: 10px 20px; font-weight: bold; cursor: pointer; min-width: 80px; }}
        
        #start-btn {{ width: 100%; padding: 15px; background: #0f0; color: #000; font-weight: bold; border: none; margin-top: 15px; cursor: pointer; font-size: 16px; }}
        .result-item {{ border: 1px solid #0f0; padding: 10px; font-size: 14px; margin-top: 10px; background: rgba(0, 30, 0, 0.9); text-align: left; }}
    </style>
</head>
<body>
<div class="overlay">
    <div class="header">
        <div class="banner-text">AFFAN</div>
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br>
        AUTHOR : {OWNER_NAME}<br>
        TOOL   : {TOOL_NAME}<br>
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    </div>

    <div class="form-box">
        <input type="password" id="pass" placeholder="ENTER PASSWORD">
        
        <div class="method-row">
            <div class="method-name">(1) OLD CLONING</div>
            <button class="btn-next" onclick="setMethod('OLD CLONING')">NEXT</button>
        </div>
        <div class="method-row">
            <div class="method-name">(2) 2014 CLONING</div>
            <button class="btn-next" onclick="setMethod('2014 CLONING')">NEXT</button>
        </div>
        <div class="method-row">
            <div class="method-name">(3) 2009 CLONING</div>
            <button class="btn-next" onclick="setMethod('2009 CLONING')">NEXT</button>
        </div>
        <div class="method-row">
            <div class="method-name">(4) EXIT</div>
            <button class="btn-exit" onclick="window.close()">EXIT</button>
        </div>

        <input type="hidden" id="selected_method" value="OLD CLONING">
        <button id="start-btn" onclick="runTool()">START CLONING</button>
    </div>

    <div id="status" style="margin-top: 15px; font-weight: bold; color: yellow;"></div>
    <div id="logs"></div>
</div>

<script>
    function setMethod(m) {{
        document.getElementById('selected_method').value = m;
        document.getElementById('status').innerHTML = "[*] Selected: " + m;
    }}

    function runTool() {{
        const p = document.getElementById('pass').value;
        const m = document.getElementById('selected_method').value;
        const logBox = document.getElementById('logs');
        const statusBox = document.getElementById('status');

        if(p !== "{FIXED_PASSWORD}") {{ 
            alert("WRONG PASSWORD!"); 
            return; 
        }}

        statusBox.innerHTML = "[*] Extracting IDs...";

        fetch('/api/crack', {{
            method: 'POST',
            headers: {{'Content-Type': 'application/x-www-form-urlencoded'}},
            body: `method=${{m}}`
        }})
        .then(res => res.json())
        .then(data => {{
            statusBox.innerHTML = "<span style='color:#0f0'>[✓] ID SUCCESS!</span>";
            let html = `
                <div class="result-item">
                    <b style="color:#0f0">[AFFAN-OK]</b> ${{data.id_data}}<br>
                    <b style="color:yellow">METHOD:</b> ${{data.year}}
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
    return jsonify({"id_data": id_data, "year": method})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
