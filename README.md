# Jenkins, GitHub, and Webex CI/CD Demonstration

This project demonstrates an automated CI/CD pipeline.

A GitHub push sends a webhook through ngrok to Jenkins. Jenkins checks out
the code, runs the build and unit-test scripts, and sends the result to a
Webex space using a Webex bot.