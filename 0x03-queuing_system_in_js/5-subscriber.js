import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// subscribing to holberton school channel
client.subscribe('holberton school channel');
client.on('message', (channel, message) => {
  if (message !== 'KILL_SERVER') {
    console.log(message);
  } else {
    client.unsubscribe('holberton school channel');
    client.end(true);
  }
});
