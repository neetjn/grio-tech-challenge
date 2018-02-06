const path = require('path')
const googleFontsPlugin = require('google-fonts-webpack-plugin')

module.exports = {
  entry: './grio.js',
  output: {
    path: path.join(__dirname, './dist'),
    publicPath: 'dist/',
    filename: 'app.js'
  },
  resolve: {
    extensions: ['.js', '.vue', '.json', '.scss'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
      '@':  path.join(__dirname, './'),
      'styles': path.join(__dirname, './assets/styles'),
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
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
            js: 'babel-loader',
            scss: [
              'vue-style-loader!css-loader!sass-loader',
              {
                loader: 'sass-resources-loader',
                options: {
                  resources: path.join(__dirname, './assets/styles/main.scss')
                }
              }
            ]
          }
        }
      },
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
          options: {
            babelrc: false,
            presets: ['env']
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
      { test: /\.html$/, loader: 'raw-loader' },
      { test: /\.(png|jpe|jpg|woff|woff2|eot|ttf|svg)(\?.*$|$)/, loader: 'url-loader' },
      { test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: 'file-loader' }
    ]
  }
}
