import { NavLink } from "react-router-dom";
import { FaHome, FaUserMd, FaRobot } from "react-icons/fa";

export default function Sidebar() {
  return (
    <div
      style={{
        width: "240px",
        height: "100vh",
        background: "#0d6efd",
        color: "white",
        padding: "25px",
        position: "fixed",
      }}
    >
      <h3>AI CRM</h3>

      <hr />

      <p>
        <NavLink
          to="/"
          style={{ color: "white", textDecoration: "none" }}
        >
          <FaHome /> Dashboard
        </NavLink>
      </p>

      <p>
        <NavLink
          to="/interactions"
          style={{ color: "white", textDecoration: "none" }}
        >
          <FaUserMd /> Interactions
        </NavLink>
      </p>

      <p>
        <NavLink
          to="/chat"
          style={{ color: "white", textDecoration: "none" }}
        >
          <FaRobot /> AI Chat
        </NavLink>
      </p>
    </div>
  );
}