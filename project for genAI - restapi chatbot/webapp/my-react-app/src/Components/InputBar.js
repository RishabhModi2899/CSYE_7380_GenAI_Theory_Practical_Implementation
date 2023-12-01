import React, { useState } from "react";
import axios from "axios";

function InputBar({ onNewMessage }) {
  const [input, setInput] = useState("");

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleSend = async () => {
    if (input.trim() !== "") {
      try {
        const payload = {
          user_input: input,
        };

        const response = await axios.post("/handle-request/", payload, {
          headers: {
            "Content-Type": "application/json",
          },
        });
        
        onNewMessage(response.data);

        setInput("");
      } catch (error) {
        console.error("Error sending message:", error);
      }
    }
  };

  return (
    <div className="input-bar">
      <input type="text" value={input} onChange={handleInputChange} />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default InputBar;
