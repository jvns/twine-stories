const http = require('http')
const fs = require('fs').promises

var start;

async function uploadFile(filename) {
    const req = http.request({ hostname: 'mysterybox', port: 8000, method: 'POST'}, res => {
        console.log("Time elapsed:", new Date() - start, "milliseconds");
    })
    const stats = await fs.stat(filename)
    start = new Date();
    req.setHeader('Content-Type', 'text/plain');
    req.setHeader('Content-Length', stats.size);
    req.flushHeaders();
    const data = await fs.readFile(filename, 'utf8');
    await new Promise(resolve => {req.write(data, resolve)});
}

uploadFile("test.txt")
