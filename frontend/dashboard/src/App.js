import React, { useEffect, useState } from "react";

function App() {

  const [fleet, setFleet] = useState([
    {equipment:"Truck-101",status:"Operational",location:"Pit A"},
    {equipment:"Drill-22",status:"Maintenance",location:"Pit B"},
    {equipment:"Excavator-9",status:"Operational",location:"Pit C"}
  ]);

  useEffect(() => {
    fetch("http://localhost:8000/fleet")
      .then(res => res.json())
      .then(data => setFleet(data))
      .catch(() => {
        console.log("API not connected — using demo data");
      });
  }, []);

  return (
    <div style={{background:"#0b1220",color:"white",minHeight:"100vh",padding:"40px",fontFamily:"Arial"}}>
      
      <h1>Mining Intelligence Platform</h1>
      <h3>Fleet Operations Dashboard</h3>

      <table style={{width:"100%",marginTop:"20px",borderCollapse:"collapse"}}>
        <thead>
          <tr style={{background:"#1c2541"}}>
            <th>Equipment</th>
            <th>Status</th>
            <th>Location</th>
          </tr>
        </thead>

        <tbody>
          {fleet.map((f,i)=>(
            <tr key={i}>
              <td>{f.equipment}</td>
              <td>{f.status}</td>
              <td>{f.location}</td>
            </tr>
          ))}
        </tbody>
      </table>

    </div>
  );
}

export default App;
