// extract.mjs
import https from 'https';

const args = process.argv.slice(2);
const url = args[0];

if (!url) {
  console.error("Usage: node extract.mjs <url>");
  process.exit(1);
}

const apiKey = process.env.TAVILY_API_KEY;
if (!apiKey) {
  console.error("Error: TAVILY_API_KEY environment variable is missing.");
  process.exit(1);
}

const data = JSON.stringify({
  api_key: apiKey,
  urls: [url]
});

const options = {
  hostname: 'api.tavily.com',
  path: '/extract',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': data.length
  }
};

const req = https.request(options, res => {
  let body = '';
  res.on('data', chunk => body += chunk);
  res.on('end', () => {
    if (res.statusCode === 200) {
      const response = JSON.parse(body);
      console.log(JSON.stringify(response, null, 2));
    } else {
      console.error(`Error: ${res.statusCode} - ${body}`);
      process.exit(1);
    }
  });
});

req.on('error', e => {
  console.error(e);
  process.exit(1);
});

req.write(data);
req.end();
