const http = require('http')

const data = JSON.stringify({
  todo: 'Buy the milk'
})

var start;
start = new Date();

const options = {
  hostname: 'mystery.local',
  port: 8000,
  path: '/todos',
  method: 'POST',
}

const req = http.request(options, res => {
  console.log(`statusCode: ${res.statusCode}`)
    console.log(new Date() - start);

  res.on('data', d => {
    //rocess.stdout.write(d)
  })
})

req.setHeader('Content-Type', 'application/json');
req.setHeader('Content-Length', data.length);
req.flushHeaders();

//req.on('error', error => {
//  console.error(error)
//})

setImmediate(() => req.write(data, () => req.end()));
