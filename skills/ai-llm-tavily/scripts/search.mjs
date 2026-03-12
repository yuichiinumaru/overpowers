// search.mjs
import https from 'https';

const args = process.argv.slice(2);
const query = args[0];
let limit = 5;
let searchDepth = "basic";
let topic = "general";
let days = 3;

for (let i = 1; i < args.length; i++) {
  if (args[i] === '-n' || args[i] === '--max-results') limit = parseInt(args[++i], 10);
  else if (args[i] === '--deep') searchDepth = "advanced";
  else if (args[i] === '--topic') topic = args[++i];
  else if (args[i] === '--days') days = parseInt(args[++i], 10);
}

if (!query) {
  console.error("Usage: node search.mjs <query> [options]");
  process.exit(1);
}

const apiKey = process.env.TAVILY_API_KEY;
if (!apiKey) {
  console.error("Error: TAVILY_API_KEY environment variable is missing.");
  process.exit(1);
}

const data = JSON.stringify({
  api_key: apiKey,
  query,
  search_depth: searchDepth,
  topic,
  max_results: limit,
  days
});

const options = {
  hostname: 'api.tavily.com',
  path: '/search',
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
