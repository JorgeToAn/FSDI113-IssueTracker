# FSDI113 - Issue Tracker

This projects presents a Django application as the competency report for FSDI113.

## Functionality

On the project you are able to create a user (username, password), then you can log in into the page with your user.

Once you're logged in you can start creating issues to track, each issue contains the following fields:

- Title
- Summary
- Description
- Status (to do, in progress, done)
- Requester (author)
- Assignee (person assigned to work on the issue)

Additionally, you can view the issues created in a list style, you can filter through the three different status.

### Change Password

You are able to change the password for your user, to do this you need to be logged in and click on the account dropdown and then select the "Change Password" option, you'll be prompted to enter your old password along with your new password.

### Reset Password

If you forget the password for your user, you are able to reset your password if your account has an email configured, you'll need to enter the email address and after that an email will be sent detailing how to reset your password.
