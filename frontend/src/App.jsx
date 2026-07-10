import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Interactions from "./pages/Interactions";
import AIChat from "./pages/AIChat";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/interactions" element={<Interactions />} />
        <Route path="/chat" element={<AIChat />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;