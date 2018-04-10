// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.
import './styles/reset.css';
import 'font-awesome/css/font-awesome.min.css'

import ReactDOM from 'react-dom';
import React from 'react';
import thunk from 'redux-thunk';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux'

import Base from './components/Base';
import reducers from './reducers';

const store = createStore(
  reducers,
  applyMiddleware(thunk)
);

ReactDOM.render(
  (<Provider store={store}>
    <Base />
  </Provider>),
  document.getElementById('root')
);