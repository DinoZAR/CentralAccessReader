const path = require('path');
const webpack = require('webpack');
const merge = require('webpack-merge');
const baseConfig = require('./webpack.config.base');

module.exports = merge.smart(baseConfig, {
  entry: path.join(__dirname, 'main.js'),
  output: {
    path: __dirname + '/build',
    publicPath: path.join(__dirname, 'src'),
    filename: 'main.js'
  },
  plugins: [
    new webpack.DefinePlugin({
      'process.env': {
        'NODE_ENV': '"electron"'
      }
    })
  ],
  target: 'electron-main',
});