import React, { useState } from "react";

function App() {

  const [company, setCompany] = useState("");

  const [logs, setLogs] = useState([]);

  const [report, setReport] = useState("");

  const startResearch = () => {

    setLogs([]);

    setReport("");

    const eventSource = new EventSource(

      `http://localhost:8000/research/${company}`
    );

    eventSource.onmessage = (event) => {

      const data = event.data;

      if (
        data.includes("FINAL_REPORT::")
      ) {

        setReport(

          data.replace(
            "FINAL_REPORT::",
            ""
          )
        );

        eventSource.close();

      } else {

        setLogs(prev => [

          ...prev,

          data
        ]);
      }
    };
  };

  return (

    <div style={{

      padding: "30px",

      fontFamily: "Arial"
    }}>

      <h1>
        Company Research Agent
      </h1>

      <input

        type="text"

        placeholder="Enter company name"

        value={company}

        onChange={(e) =>

          setCompany(e.target.value)
        }

        style={{

          padding: "10px",

          width: "300px"
        }}
      />

      <button

        onClick={startResearch}

        style={{

          padding: "10px",

          marginLeft: "10px"
        }}
      >
        Research
      </button>

      <h2>
        Agent Activity
      </h2>

      <ul>

        {logs.map((log, index) => (

          <li key={index}>
            {log}
          </li>
        ))}
      </ul>

      <h2>
        Company Portfolio
      </h2>

      <pre>
        {report}
      </pre>

      {report && (

        <a

          href={`http://localhost:8000/download/${company}`}

          target="_blank"

          rel="noreferrer"
        >
          Download Excel Report
        </a>
      )}

    </div>
  );
}

export default App;