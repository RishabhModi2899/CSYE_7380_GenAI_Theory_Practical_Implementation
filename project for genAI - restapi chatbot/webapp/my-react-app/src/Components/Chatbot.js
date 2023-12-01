
import React, { useState } from "react";
import MessageList from "./MessageList";
import InputBar from "./InputBar";

function Chatbot() {
  const [messages, setMessages] = useState([]);

  const handleNewMessage = (newMessage) => {
    setMessages([...messages, newMessage]);
  };

  return (
    <div className="chatbot">
      <MessageList messages={messages} />
      <InputBar onNewMessage={handleNewMessage} />
    </div>
  );
}

export default Chatbot;
