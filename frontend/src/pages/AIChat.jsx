import { useState } from "react";
import Sidebar from "../Sidebar";
import Navbar from "../Navbar";
import API from "../services/api";

export default function AIChat() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const sendMessage = async () => {
    if (!message) return;

    try {
      const res = await API.post("/chat", {
        message: message,
      });

      setReply(res.data.response);
    } catch (err) {
      console.error(err);
      setReply("Error connecting to AI.");
    }
  };

  return (
    <div className="d-flex">
      <Sidebar />

      <div className="flex-grow-1" style={{ marginLeft: "240px" }}>
        <Navbar />

        <div className="container mt-4">
          <h2>AI Chat</h2>

          <textarea
            className="form-control"
            rows="4"
            placeholder="Ask AI..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />

          <button
            className="btn btn-primary mt-3"
            onClick={sendMessage}
          >
            Send
          </button>

          <div className="card mt-3 p-3">
            <strong>AI Response:</strong>
            <p>{reply}</p>
          </div>
        </div>
      </div>
    </div>
  );
}