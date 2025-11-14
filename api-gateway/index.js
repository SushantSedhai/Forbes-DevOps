const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Proxy middleware options
const options = {
  target: 'http://backend:5000', // target host
  changeOrigin: true, // needed for virtual hosted sites
  pathRewrite: {
    '^/api': '', // rewrite path
  },
};

// Create the proxy
const apiProxy = createProxyMiddleware(options);

// Use the proxy
app.use('/api', apiProxy);

// Start the server
const port = 8080;
app.listen(port, () => {
  console.log(`API Gateway listening on port ${port}`);
});
