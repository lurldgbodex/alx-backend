import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));

client.on('connect', () => console.log('Redis client connected to the server'));

const key = 'HolbertonSchools';
const fields = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

fields.forEach((field, value) => {
  client.hset(key, field, values[value], print);
});

client.hgetall(key, (err, value) => {
  console.log(value);
});
