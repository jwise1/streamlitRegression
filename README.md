# streamlitRegression
Linear regression model for prediction of receipt totals for Fetch 2022. Deployed via streamlit and containerized using Docker.
TO RUN: pull image from docker hub: with docker open, run terminal command "docker pull jaredwise/lr_receipt_tracker:v1"
This pulls the deployment image to your machine to run. Then, run the command "docker run -p 8501:8501 jaredwise/lr_receipt_tracker:v1"

This allows you to navigate to a web browser and connect to the web app locally by accessing the site: "localhost:8501"

The 8501 designation is giving a specific port number to access the application on.
