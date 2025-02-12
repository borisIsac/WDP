import { useState } from "react";

const RegisterForm = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    confirm_password: "",
    full_name: "",
    phone: "",
    username: "",
    birthday: "",
    gender: "Select",
    country: "",
  });

  const [message, setMessage] = useState("");

  // ✅ Handle input changes
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // ✅ Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (formData.password !== formData.confirm_password) {
      setMessage("❌ Passwords do not match!");
      return;
    }

    const response = await fetch("http://127.0.0.1:8000/users/api/register/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });

    const data = await response.json();
    setMessage(data.message);

    if (response.ok) {
      setMessage("✅ Registration successful! Please check your email to activate your account.");
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "0 auto", padding: "20px", border: "1px solid #ccc", borderRadius: "8px" }}>
      <h1>Register</h1>
      {message && <p style={{ color: message.includes("✅") ? "green" : "red" }}>{message}</p>}

      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
        <label>Email</label>
        <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} required />

        <label>Full Name</label>
        <input type="text" name="full_name" placeholder="Full Name" value={formData.full_name} onChange={handleChange} required />

        <label>Password</label>
        <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} required />

        <label>Confirm Password</label>
        <input type="password" name="confirm_password" placeholder="Confirm Password" value={formData.confirm_password} onChange={handleChange} required />

        <label>Phone</label>
        <input type="text" name="phone" placeholder="Phone" value={formData.phone} onChange={handleChange} />

        <label>Username</label>
        <input type="text" name="username" placeholder="Username" value={formData.username} onChange={handleChange} />

        <label>Birthday</label>
        <input type="date" name="birthday" value={formData.birthday} onChange={handleChange} />

        <label>Gender</label>
        <select name="gender" value={formData.gender} onChange={handleChange}>
          <option value="Select">Select Gender</option>
          <option value="Male">Male</option>
          <option value="Female">Female</option>
        </select>

        <label>Country</label>
        <input type="text" name="country" placeholder="Country" value={formData.country} onChange={handleChange} />

        <button type="submit" style={{ padding: "10px", backgroundColor: "#007bff", color: "#fff", border: "none", borderRadius: "4px", cursor: "pointer" }}>
          Register
        </button>
      </form>
    </div>
  );
};

export default RegisterForm;