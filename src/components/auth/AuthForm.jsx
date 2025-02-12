import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

const AuthForm = ({ type }) => {
  const { token } = useParams(); // For activation links
  const navigate = useNavigate();

  // State for form inputs and messages
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [fullName, setFullName] = useState("");
  const [message, setMessage] = useState("");

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    let url = "";
    let body = {};

    if (type === "login") {
      url = "http://127.0.0.1:8000/users/api/login/";
      body = { email, password };
    } else if (type === "register") {
      url = "http://127.0.0.1:8000/users/api/register/";
      body = { email, password, confirm_password: confirmPassword, full_name: fullName };
    } else if (type === "reset_password") {
      url = "http://127.0.0.1:8000/users/api/password-reset/";
      body = { email };
    } else if (type === "activate") {
      url = `http://127.0.0.1:8000/users/api/activate/${token}/`;
      body = {};
    }

    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const data = await response.json();
    setMessage(data.message);

    if (response.ok && type === "login") {
      navigate("/dashboard"); // Redirect on successful login
    } else if (response.ok && type === "register") {
      navigate("/login"); // Redirect to login after registration
    }
  };

  return (
    <div>
      <h1>
        {type === "login"
          ? "Login"
          : type === "register"
          ? "Register"
          : type === "reset_password"
          ? "Reset Password"
          : "Activate Account"}
      </h1>
      {message && <p style={{ color: "red" }}>{message}</p>}

      <form onSubmit={handleSubmit}>
        {type !== "activate" && (
          <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        )}
        {type === "register" && (
          <input type="text" placeholder="Full Name" value={fullName} onChange={(e) => setFullName(e.target.value)} required />
        )}
        {type === "login" || type === "register" ? (
          <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        ) : null}
        {type === "register" && (
          <input type="password" placeholder="Confirm Password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} required />
        )}
        <button type="submit">
          {type === "login"
            ? "Login"
            : type === "register"
            ? "Register"
            : type === "reset_password"
            ? "Send Reset Email"
            : "Activate Account"}
        </button>
      </form>

      {type === "login" && <a href="/password-reset">Forgot password?</a>}
    </div>
  );
};

export default AuthForm;
