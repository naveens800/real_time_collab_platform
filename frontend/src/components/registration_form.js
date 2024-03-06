import React, { useState, useEffect } from 'react';
import axios from 'axios';


function HelloWorld() {
    const [message, setMessage] = useState('');
  
    useEffect(() => {
      axios.get('myapp/')
        .then(response => {
          setMessage(response.data.message);
        })
        .catch(error => {
          console.log(error);
        });
    }, []);
  
    return (
      <div>
        <h1>Hello, World!</h1>
        <h2>{message}</h2>
      </div>
    );
  }

  export default HelloWorld;
