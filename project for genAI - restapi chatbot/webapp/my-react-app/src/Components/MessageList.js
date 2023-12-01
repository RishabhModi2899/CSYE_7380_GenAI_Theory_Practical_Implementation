import React from "react";

function MessageList({ messages }) {
  const renderMessageContent = (message) => {
    
    if (typeof message.data === "string") {
      return <span>{message.data}</span>;
    }
    
    if (typeof message.data === "object") {
      const dataArray = Array.isArray(message.data)
        ? message.data
        : [message.data];
      return (
        <table>
          <thead>
            
            <tr>
              {Object.keys(dataArray[0]).map((key) => (
                <th key={key}>{key}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            
            {dataArray.map((item, index) => (
              <tr key={index}>
                {Object.values(item).map((val, idx) => (
                  <td key={idx}>
                    {typeof val === "object" ? JSON.stringify(val) : val}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      );
    }
  };

  return (
    <div className="message-list">
      {messages.map((message, index) => (
        <div key={index} className="message-item">
          {renderMessageContent(message)}
        </div>
      ))}
    </div>
  );
}

export default MessageList;
