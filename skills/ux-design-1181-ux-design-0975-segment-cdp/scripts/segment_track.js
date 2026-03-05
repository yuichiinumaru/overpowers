const { Analytics } = require('@segment/analytics-node');

const analytics = new Analytics({ writeKey: process.env.SEGMENT_WRITE_KEY });

async function trackEvent(userId, event, properties = {}) {
  try {
    analytics.track({
      userId,
      event,
      properties,
    });
    await analytics.closeAndFlush();
    console.log(`Event '${event}' tracked for user '${userId}'`);
  } catch (error) {
    console.error('Error tracking event:', error);
  }
}

async function identifyUser(userId, traits = {}) {
  try {
    analytics.identify({
      userId,
      traits,
    });
    await analytics.closeAndFlush();
    console.log(`User '${userId}' identified`);
  } catch (error) {
    console.error('Error identifying user:', error);
  }
}

if (require.main === module) {
  const args = process.argv.slice(2);
  const cmd = args[0];
  const userId = args[1];
  const data = args[2] ? JSON.parse(args[2]) : {};

  if (cmd === 'track') {
    const event = args[3] || 'Default Event';
    trackEvent(userId, event, data);
  } else if (cmd === 'identify') {
    identifyUser(userId, data);
  } else {
    console.log('Usage: node segment_track.js <track|identify> <userId> <jsonData> [eventName]');
  }
}
