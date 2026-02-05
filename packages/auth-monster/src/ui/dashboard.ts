import blessed from 'blessed';
const contrib = require('blessed-contrib');
import { AuthMonster } from '../index';

export function startDashboard(monster: AuthMonster) {
  const screen = blessed.screen({
    smartCSR: true,
    title: 'Auth Monster Dashboard'
  });

  const grid = new contrib.grid({rows: 12, cols: 12, screen: screen});

  // Health Gauge
  const gauge = grid.set(0, 0, 4, 4, contrib.gauge, {
    label: 'System Health',
    percent: [0],
    stroke: 'green',
    fill: 'white'
  });

  // Status Log
  const log = grid.set(0, 4, 4, 8, contrib.log, {
    fg: 'green',
    selectedFg: 'green',
    label: 'Activity Log'
  });

  // Accounts Table
  const table = grid.set(4, 0, 8, 12, contrib.table, {
    keys: true,
    fg: 'white',
    selectedFg: 'white',
    selectedBg: 'blue',
    interactive: true,
    label: 'Accounts',
    width: '30%',
    height: '30%',
    border: {type: 'line', fg: 'cyan'},
    columnSpacing: 10,
    columnWidth: [15, 30, 10, 10, 20]
  });

  screen.key(['escape', 'q', 'C-c'], function(ch: any, key: any) {
    return process.exit(0);
  });

  // Initial render
  updateDashboard();

  // Periodic update
  setInterval(updateDashboard, 1000);

  async function updateDashboard() {
    await monster.init();
    const accounts = monster.getAllAccountsStatus();

    // Update Gauge
    const total = accounts.length;
    const healthy = accounts.filter(a => a.isHealthy).length;
    const healthPercent = total > 0 ? Math.round((healthy / total) * 100) : 0;
    gauge.setPercent(healthPercent);

    // Update Table
    const tableData = accounts.map(a => [
        a.provider,
        a.email,
        a.isHealthy ? 'Healthy' : 'Unhealthy',
        a.healthScore.toString(),
        a.lastUsed ? new Date(a.lastUsed).toLocaleTimeString() : 'Never'
    ]);

    table.setData({
        headers: ['Provider', 'Email', 'Status', 'Score', 'Last Used'],
        data: tableData
    });

    screen.render();
  }

  log.log('Dashboard started...');
  log.log(`Monitoring ${monster.getAccounts().length} accounts.`);
}
