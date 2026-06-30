import { useState } from "react";
import axios from "axios";
import "./App.css"

// CORS cross origin resorce sharing 

function App(){
  const [prompt, setPrompt] = useState("");
  const [output, setOutput] = useState("");
  function handleChange(event){
    setPrompt(event.target.value);
  };

  async function GenerateResponse() {
  const res = await axios.post("http://localhost:8000/generate", {
    prompt: prompt,
  });

  setOutput(res.data.response);
}

  return(
    <div>
      <h1>404 Brain Found</h1>
      <textarea onChange={handleChange} placeholder="Enter your prompt"></textarea>
      <button onClick={GenerateResponse}>Generate Response</button>
      <div className="response-box">
        <h2>Gemini Response</h2>
        <p>{output}</p>
      </div>

    </div>
  )
}


export default App