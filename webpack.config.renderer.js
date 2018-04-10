const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const merge = require('webpack-merge');
const webpack = require('webpack');
const baseConfig = require('./webpack.config.base');

module.exports = merge.smart(baseConfig, {
  entry: path.join(__dirname + '/ui/renderer.js'),
  target: 'electron-renderer',
  output: {
    path: __dirname + '/build',
    publicPath: 'http://localhost:8080/build/',
    filename: 'renderer.js'
  },
  plugins: [
    new webpack.DefinePlugin({
      'process.env': {
        'NODE_ENV': '"web"'
      }
    }),
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
});

