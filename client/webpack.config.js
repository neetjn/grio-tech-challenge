const path = require('path')
const googleFontsPlugin = require('google-fonts-webpack-plugin')

module.exports = {
  entry: './App.jsx',
  output: {
    path: path.join(__dirname, './dist'),
    publicPath: 'dist/',
    filename: 'app.js',
  },
  resolve: {
    alias: {
      'react': 'preact-compat',
      'react-dom': 'preact-compat',
      // Not necessary unless you consume a module using `createClass`
      'create-react-class': 'preact-compat/lib/create-react-class'
    }
  },
  externals : {
    document: 'document'
  },
  plugins: [
    new googleFontsPlugin({
			fonts: [
				{ family: 'Ubuntu' },
        { family: 'Rubik Mono One' }
			]
		})
  ],
  module: {
    rules: [
      {
        test: /\.js|.jsx$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
          options: {
            babelrc: false,
            presets: ['react', 'env']
          }
        }
      },
      {
        test: /\.s[a|c]ss$/,
        use: [
          { loader: 'style-loader' },
          { loader: 'css-loader' },
          { loader: 'sass-loader' }
        ]
      },
      {
        test: /\.css$/,
        use: [
          { loader: 'style-loader' },
          { loader: 'css-loader' }
        ]
      },
      { test: /\.html$/, loader: 'raw-loader'},
      { test: /\.(png|jpe|jpg|woff|woff2|eot|ttf|svg)(\?.*$|$)/, loader: 'url-loader' },
      { test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: 'file-loader' }
    ]
  }
}
