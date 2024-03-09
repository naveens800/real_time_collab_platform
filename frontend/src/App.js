import './App.css';
import { LoginForm, GoogleLoginButton } from './components/Login';

function App() {
  return (
    <div>
      <h1>Welcome to my App</h1>
      <LoginForm />
      <GoogleLoginButton />
    </div>
  );
  
}

export default App;
