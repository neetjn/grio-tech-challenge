import { h, Component } from 'preact'
import { Router } from 'react-router'

import { Header } from './components/Header.jsx'
import { Home } from './routes/Home.jsx'
import { Search } from './routes/Search.jsx'

export default class App extends Component {

	render() {
		return (
			<App>
				<Header />
				<Router onChange={this.handleRoute}>
					<Home path="/" />
					<Search path="/search/" />
				</Router>
			</App>
		)
  }

}
