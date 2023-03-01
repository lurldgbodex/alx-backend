import { createQueue } from 'kue';

const queue = createQueue();

const blacklist = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.progress(50, 100);
  console.log(`sending notification to ${phoneNumber}, with message ${message}`);
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { data } = job;
  sendNotification(data.phoneNumber, data.message, job, done);
});
