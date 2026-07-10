export default function Navbar() {
  return (
    <nav
      className="navbar navbar-expand-lg bg-white shadow-sm"
      style={{
        height: "70px",
        padding: "0 30px",
      }}
    >
      <div className="container-fluid">

        <h3
          className="mb-0 fw-bold"
          style={{ color: "#0d6efd" }}
        >
          AI First CRM
        </h3>

        <div className="d-flex align-items-center">

          <span className="me-3 text-secondary">
            Welcome
          </span>

          <img
            src="https://ui-avatars.com/api/?name=Admin&background=0d6efd&color=fff"
            alt="Profile"
            width="40"
            height="40"
            className="rounded-circle"
          />

        </div>

      </div>
    </nav>
  );
}