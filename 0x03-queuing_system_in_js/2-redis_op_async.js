import { createClient, print } from 'redis';

const util = require('util');

const client = createClient();
client.get = util.promisify(client.get);

client.on('error', (err) => console.log('Redis client not connected to the server:', err));

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const value = await client.get(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
