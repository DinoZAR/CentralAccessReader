const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: path.join(__dirname + '/ui/renderer.js'),
  output: {
    publicPath: '/',
    path: path.join(__dirname + '/dist'),
    filename: '[name].js'
  },
  devtool: 'source-map',
  module: {
    loaders: [
      { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
      { test: /\.jsx$/, loader: 'babel-loader', exclude: /node_modules/ },
      {
        test: /\.(css|min\.css)$/,
        use: ['style-loader', 'css-loader']
      },
      // {
      //   test: /\.(png|jpg|gif|woff|woff2|ttf|eot|svg)$/,
      //   use: ['file-loader']
      // }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.join(__dirname + '/ui/index.html'),
      filename: 'index.html',
      inject: true,
      appMountID: 'root'
    })
  ],
  devServer: {
    historyApiFallback: true,
    port: 8080,
  }
}
