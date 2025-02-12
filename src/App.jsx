import { BrowserRouter as Router, Route, Routes, Navigate, Link } from "react-router-dom";
import { useState, useEffect } from "react";
import RegisterForm from "./components/auth/RegisterForm";
import Login from "./components/auth/Login"; // Import the Login component
import AuthForm from "./components/auth/AuthForm"; 

function App() {
  const [message, setMessage] = useState("Connecting...");

  // ✅ Test Connection to Django Backend
  useEffect(() => {
    fetch("http://127.0.0.1:8000/users/api/test/")
      .then((res) => {
        if (!res.ok) throw new Error("Server response was not OK");
        return res.json();
      })
      .then((data) => setMessage(data.message || "Django Connected! ✅"))
      .catch((error) => {
        console.error("Error fetching API:", error);
        setMessage("⚠️ Backend Offline - Check Django Server!");
      });
  }, []);

  return (
    <Router>
      <div>
        {/* ✅ Backend Connection Status */}
        <p style={{ color: message.includes("Offline") ? "red" : "green" }}>
          Backend says: {message}
        </p>

        {/* ✅ Login & Register Buttons */}
        <nav>
          <Link to="/login">
            <button>Login</button>
          </Link>
          <Link to="/register">
            <button>Register</button>
          </Link>
        </nav>

        {/* ✅ Routes */}
        <Routes>
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/login" element={<Login />} /> {/* Use Login component */}
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/password-reset" element={<AuthForm type="reset_password" />} />
          <Route path="/activate/:token" element={<AuthForm type="activate" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;