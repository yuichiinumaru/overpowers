import express from 'express';
import { AuthMonster } from '../index';

export function startServer(monster: AuthMonster, port: number = 3000) {
  const app = express();

  app.get('/', (req, res) => {
    res.send(`
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auth Monster Dashboard</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #1e1e1e; color: #fff; margin: 0; padding: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { text-align: left; padding: 12px; border-bottom: 1px solid #333; }
        th { background-color: #2d2d2d; }
        tr:hover { background-color: #2d2d2d; }
        .healthy { color: #4caf50; }
        .unhealthy { color: #f44336; }
        .card { background: #252526; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
        h1 { margin-top: 0; }
        .refresh-btn { float: right; padding: 8px 16px; background: #007acc; color: white; border: none; border-radius: 4px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <button class="refresh-btn" onclick="fetchData()">Refresh</button>
        <h1>Auth Monster Dashboard</h1>
        <div id="status">Loading...</div>
    </div>

    <div class="card">
        <h2>Accounts</h2>
        <table id="accounts">
            <thead>
                <tr>
                    <th>Provider</th>
                    <th>Email</th>
                    <th>Status</th>
                    <th>Health Score</th>
                    <th>Last Used</th>
                </tr>
            </thead>
            <tbody></tbody>
        </table>
    </div>

    <script>
        async function fetchData() {
            try {
                const response = await fetch('/api/status');
                const data = await response.json();

                document.getElementById('status').innerText = \`Total Accounts: \${data.totalAccounts} | Healthy: \${data.healthyAccounts}\`;

                const tbody = document.querySelector('#accounts tbody');
                tbody.innerHTML = '';

                data.accounts.forEach(acc => {
                    const row = document.createElement('tr');
                    row.innerHTML = \`
                        <td>\${acc.provider}</td>
                        <td>\${acc.email}</td>
                        <td class="\${acc.isHealthy ? 'healthy' : 'unhealthy'}">\${acc.isHealthy ? 'Healthy' : 'Unhealthy'}</td>
                        <td>\${acc.healthScore}</td>
                        <td>\${acc.lastUsed ? new Date(acc.lastUsed).toLocaleString() : 'Never'}</td>
                    \`;
                    tbody.appendChild(row);
                });
            } catch (e) {
                console.error(e);
            }
        }

        fetchData();
        setInterval(fetchData, 2000);
    </script>
</body>
</html>
    `);
  });

  app.get('/api/status', async (req, res) => {
    // Reload accounts to get latest state from disk
    await monster.init();
    const accounts = monster.getAllAccountsStatus();
    res.json({
      totalAccounts: accounts.length,
      healthyAccounts: accounts.filter(a => a.isHealthy).length,
      accounts
    });
  });

  app.listen(port, '127.0.0.1', () => {
    console.log(`Web Admin Dashboard running at http://127.0.0.1:${port}`);
  });
}
