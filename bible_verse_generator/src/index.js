import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
export { default as Home } from './routes/Home';

ReactDOM.render(
    <App />
,
  document.getElementById('root')
);

reportWebVitals();
