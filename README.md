# streamlitRegression
Linear regression model for prediction of receipt totals for Fetch 2022. Deployed via streamlit and containerized using Docker.

TO RUN: pull image from docker hub--with docker open, run terminal command "docker pull jaredwise/lr_receipt_tracker:v1"
This pulls the deployment image to your machine to run. Then, run the command "docker run -p 8501:8501 jaredwise/lr_receipt_tracker:v1"
This allows you to navigate to a web browser and connect to the web app locally by accessing the site: "localhost:8501"
The 8501 designation is giving a specific port number to access the application on. This is a specification chosen when creating the dockerfile.

Machine learning development:
In creating the application, I started by employing a simple linear regression model since the data given has a linear structure. My first step in deciding algorithms for machine learning is understanding the properties of the data. After seeing linearity, I know that a simple regression model can manage this well. By fitting the data to a linear equation and training the model on the data by optimizing the weight and bias value of the equation, we can find an equation that works for any x and returns a calculated value for prediction. By injecting non-linearity into the function or by using advanced techniques to map the input, we can further account for months such as February where there was a slight decline in receipt totals. This wasn't accomplished through my model and would require more than the time already put into this development, however it's more than possible with more time. In training the model, what we are really doing is finding optimal values of the weight and bias. As such, we save these values serialized and use them within our web application to produce prediction values. By feeding our input as a month to the equation we can predict future month receipt totals. 

Web app development: 
Streamlit is a web app deployment tool that I used to leverage the equation and model created from the data provided. By deserializing the optimal values trained from the data, we can use these to make predictions through a user friendly web application. Further, we can illustrate the problem environment and better understand the purpose of the problem/solution set through these visualizations such as graphs, images, etc. 

Docker image development:
In accessing the web application in different systems, we need to be sure the dependencies used when testing are available to the user trying to access the application. To do this, docker is a useful tool to containerize an environment for different systems. I created a docker image that then was stored in a container that you can now access from the DockerHub from my profile. The steps listed above will allow you to pull and run the container to see the results in your local environment.
