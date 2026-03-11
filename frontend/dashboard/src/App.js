
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return '''
    <html>
    <head>
        <title>InterMineForce360</title>
        <style>
            body {
                font-family: Arial;
                background:#0f172a;
                color:white;
                padding:40px;
            }
            h1 {color:#38bdf8;}
            table {
                width:100%;
                border-collapse:collapse;
                margin-top:20px;
            }
            th,td {
                border:1px solid #334155;
                padding:10px;
                text-align:left;
            }
            th {background:#1e293b;}
        </style>
    </head>
    <body>
        <h1>InterMineForce360</h1>
        <h2>Mining Intelligence Dashboard</h2>

        <table>
            <tr>
                <th>Equipment</th>
                <th>Status</th>
                <th>Location</th>
            </tr>
            <tr>
                <td>Truck-101</td>
                <td>Operational</td>
                <td>Pit A</td>
            </tr>
            <tr>
                <td>Drill-22</td>
                <td>Maintenance</td>
                <td>Pit B</td>
            </tr>
            <tr>
                <td>Excavator-9</td>
                <td>Operational</td>
                <td>Pit C</td>
            </tr>
        </table>

        <h3>Predictive Maintenance</h3>
        <p>AI Risk Score: 32%</p>

        <h3>Operational Resilience</h3>
        <p>Supply Chain Stability Index: 87%</p>

    </body>
    </html>
    '''

@app.get("/fleet")
def fleet():
    return [
        {"equipment":"Truck-101","status":"Operational","location":"Pit A"},
        {"equipment":"Drill-22","status":"Maintenance","location":"Pit B"},
        {"equipment":"Excavator-9","status":"Operational","location":"Pit C"}
    ]
