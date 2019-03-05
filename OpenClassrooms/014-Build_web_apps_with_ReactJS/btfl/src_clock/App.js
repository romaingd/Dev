import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Clock from './Clock';
import ClickMeButton from './ClickMeButton';
import ColoredBlock from './ColoredBlock';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>

        <p className="App-intro">
          Hi {this.props.name}!
        </p>
        <ClickMeButton></ClickMeButton>
        <Clock></Clock>

        <div className="main-content">
          <ColoredBlock />
        </div>

        <footer>...</footer>
      </div>
    );
  }
}

export default App;
