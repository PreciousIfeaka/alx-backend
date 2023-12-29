import { createQueue } from 'kue';

const blackLists = ['4153518780', '4153518781'];

const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blackLists.includes(phoneNumber)) {
    return done(new Error(`phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(50, 100);
  console.log(`sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, done);
});
