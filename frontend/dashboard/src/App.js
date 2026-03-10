
import React, {useEffect, useState} from "react";

function App() {

  const [fleet, setFleet] = useState([])

  useEffect(()=>{
    fetch("http://localhost:8000/fleet")
      .then(r=>r.json())
      .then(setFleet)
  },[])

  return (
    <div style={{padding:40,fontFamily:"Arial"}}>
      <h1>Mining Intelligence Dashboard</h1>
      <h2>Fleet Status</h2>
      <table border="1" cellPadding="8">
        <thead>
          <tr>
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
  )
}

export default App
