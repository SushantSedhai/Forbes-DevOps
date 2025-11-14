import React from 'react';
import './App.css';

function App() {
  const handleLoginClick = () => {
    window.location.href = '/login';
  };

  return (
    <div className="App">
      <header className="App-header">
        <nav>
          <button onClick={handleLoginClick} className="login-button">Login</button>
        </nav>
      </header>
      <main>
        <h1>Welcome to Our Page</h1>
      </main>
    </div>
  );
}

export default App;
