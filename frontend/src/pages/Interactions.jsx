import Sidebar from "../Sidebar";
import Navbar from "../Navbar";

export default function Interactions() {
  return (
    <div className="d-flex">
      <Sidebar />

      <div className="flex-grow-1" style={{ marginLeft: "240px" }}>
        <Navbar />

        <div className="container mt-4">
          <h2>Interactions</h2>

          <div className="card p-4">
            <h5>Log HCP Interaction</h5>
            <p>This page will be used to log doctor interactions.</p>
          </div>
        </div>
      </div>
    </div>
  );
}