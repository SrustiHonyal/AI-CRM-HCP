import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { setInteractions } from "../redux/interactionSlice";
import API from "../services/api";

import Sidebar from "../Sidebar";
import Navbar from "../Navbar";

export default function Dashboard() {
  const dispatch = useDispatch();

  const interactions = useSelector(
    (state) => state.interactions.list
  );

  useEffect(() => {
    API.get("/interactions/")
      .then((res) => {
        dispatch(setInteractions(res.data));
      })
      .catch((err) => {
        console.error(err);
      });
  }, [dispatch]);

  return (
    <div>
      <Sidebar />

      <div
        style={{
          marginLeft: "240px",
          minHeight: "100vh",
          background: "#f8f9fa",
        }}
      >
        <Navbar />

        <div className="container py-4">
          <div className="card shadow-sm p-3 mb-4">
            <h5>Total Interactions: {interactions.length}</h5>
          </div>

          <div className="card shadow-sm">
            <div className="card-body">
              <table className="table table-hover">
                <thead>
                  <tr>
                    <th>Doctor</th>
                    <th>Hospital</th>
                    <th>Product</th>
                    <th>Visit Date</th>
                  </tr>
                </thead>

                <tbody>
                  {interactions.map((item) => (
                    <tr key={item.id}>
                      <td>{item.doctor_name}</td>
                      <td>{item.hospital}</td>
                      <td>{item.product}</td>
                      <td>{item.visit_date}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
}