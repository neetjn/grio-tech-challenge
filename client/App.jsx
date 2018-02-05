import React, { Component } from 'react'
import { HashRouter } from 'react-router-dom'

import { Header } from './components/Header.jsx'
import { Home } from './routes/Home.jsx'
import { Search } from './routes/Search.jsx'

export class App extends Component {

	render() {
		return (
      <app>
				<Header />
				<HashRouter>
          <div id="view">
            <Home path="/" />
            <Search path="/search/" />
          </div>
				</HashRouter>
      </app>
		)
  }

}
