function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const newJob = queue.create('push_notification_code_3', job);
    newJob.save((error) => {
      if (!error) { console.log(`Notification job created: ${newJob.id}`); }
    });
    newJob.on('complete', () => console.log(`Notification job ${newJob.id} completed`));
    newJob.on('failed', (error) => console.error(`Notification job ${newJob.id} failed: ${error}`));
    newJob.on('progress', (progress) => console.log(`Notification job ${newJob.id} ${progress}% complete`));
  });
}

module.exports = createPushNotificationsJobs;
