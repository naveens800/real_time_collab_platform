import React, { useState } from 'react'
import { useMutation } from '@apollo/client';
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';
import { LOGIN_MUTATION, GOOGLE_LOGIN } from '../graphql/mutations';





export function GoogleLoginButton(){
  const [googleLogin, { data, error }] = useMutation(GOOGLE_LOGIN)
  const handleSuccess = (response) => {
    googleLogin({variables: { token:response.credential }})
  }
  const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID;
  const handleError = () => {
    console.log("Login Failed", error)
  }

  return (
    <GoogleOAuthProvider clientId={clientId}>
      <GoogleLogin onSuccess={handleSuccess} onError={handleError} />
    </GoogleOAuthProvider>
  )
}


export function LoginForm() {
    // Use state to manage input values
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [login, { data, loading, error }] = useMutation(LOGIN_MUTATION);
  const [loginMessage, setLoginMessage] = useState('');


  // Handle input change for username
  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  // Handle input change for password
  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    // Implement form submission logic here (e.g., validation, login)
    const username = event.target.username.value
    const password = event.target.password.value
    
    if (loading) return 'Submitting...';
    if (error) return `Submission error! ${error.message}`;

    try {
      const { data } = login({ variables: { username, password } });
      setLoginMessage("Log In Successful")
      console.log(data)
    } catch (error){
      console.log("Error Occurred In Login Function",error)
    }
  };

  return (
    <div>
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="username">Username:</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={handleUsernameChange}
              required
            />
          </div>
          <div>
            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={handlePasswordChange}
              required
            />
          </div>
          <button type="submit">Login</button>
        </form>
        {loginMessage && <p>{loginMessage}</p>}
      {error && <p style={{ color: 'red' }}>An error occurred during login: {error.message}</p>}

    </div>
  )
}

