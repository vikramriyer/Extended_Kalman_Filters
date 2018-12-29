# Extended Kalman Filter

In this project we will utilize a kalman filter to estimate the state of a moving object of interest with noisy lidar and radar measurements.
We will use RMSE as the error metric.

---

### Q. What is a kalman filter?
It's a repetitive/iterative mathematical process that has some inputs plugged into equations to predict/estimate the next value in terms of position, velocity, etc of any object being measured, when the measured values contain unpredicted errors, uncertainty, or variation.

I am sure, an application based explanation would help you understand its usage better.

Suppose that we are building a self-driving car, and for this, we are using sensors to track the pedestrians, vehicles, objects on the road. Now, at every instance, we get a reading from the sensors. Now, our task is to make the car ride on the road without colliding. So, primarily we need to tell the car, what its position and velocity should be at t+1 where t is the current instance. We use the measurements from the sensors and a bunch of equations to predict what the next position and velocity of the car should be. This prediction of position and velocity happens till we reach the destination which means its an iterative/repetitive/continuous process as mentioned in the formal definition. <br>
Now, there are some errors when we depend on sensors, there are errors when mathematical calculations are involved. So, the kalman filter also has a solution to rectify the noise/error (not completely but to a manageable extent).
