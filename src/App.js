import './App.css';
import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Link, BrowserRouter } from 'react-router-dom';
import { Home } from './index'


export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {

    }
  }

  render = () => {
    return (
      <BrowserRouter>
        <div className="App">
          <Route exact path="/" component={Home}></Route>
        </div>
      </BrowserRouter>
    )
  }
}