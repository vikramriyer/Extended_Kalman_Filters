# Extended Kalman Filter

In this project we will utilize a kalman filter to estimate the state of a moving object of interest with noisy lidar and radar measurements.
We will use RMSE as the error metric.

---

__Q. What is a kalman filter?__ <br>
It's a repetitive/iterative mathematical process that has some inputs plugged into equations to predict/estimate the next value in terms of position, velocity, etc of any object being measured, when the measured values contain unpredicted errors, uncertainty, or variation.

I am sure, an application based explanation would help you understand its usage better.

Suppose that we are building a self-driving car, and for this, we are using sensors to track the pedestrians, vehicles, objects on the road. Now, at every instance, we get a reading from the sensors. Now, our task is to make the car ride on the road without colliding. So, primarily we need to tell the car, what its position and velocity should be at t+1 where t is the current instance. We use the measurements from the sensors and a bunch of equations to predict what the next position and velocity of the car should be. This prediction of position and velocity happens till we reach the destination which means its an iterative/repetitive/continuous process as mentioned in the formal definition. <br>
Now, there are some errors when we depend on sensors, there are errors when mathematical calculations are involved. So, the kalman filter also has a solution to rectify the noise/error (not completely but to a manageable extent).

__Q. What is a typical workflow of the entire process?__ <br>
1. calculate the kalman gain
2. calculate the current estimate
3. recalculate the new error in the estimate
4. repeat the process(1-3) iteratively

_Calculate the Kalman Gain_ <br>
In this step, we use the error in estimate (our calculations) and error in data (measurements, sensor specific) to find the kalman gain. We give more emphasis to the error that is minimum as it would contribute better to ensure we stay close to the actual/true value.

_Calculate the Current Estimate_ <br>
We have the kalman gain that we calculated in the previous step. This kalman gain is fed to the next step along with the previous estimate and the stream of input data we receive at each instance, we calculate the current estimate. The kalman gain will decide how much weight to put on estimate or the input data. So the task of the kalman gain is to put relative importance on the previous estimate and input data.

_Calculate the Error in the Estimate_ <br>
We use the calculated current estimate and the kalman gain to find out the error so that we can feed it back when calculating the kalman gain for the next instance of time.

Now for each of the above step, we get an estimate which says how the object should be moving. Let's look at the mathematics behind this in the below sections.

#### Kalman Gain Calculation

KG = Kalman Gain <br>
E<sub>est</sub> = Error in estimate <br>
E<sub>mea</sub> = Error in data (measurement) <br>

KG = E<sub>est</sub> / (E<sub>est</sub> + E<sub>mea</sub>)

0 <= KG <= 1

#### Current Estimate Calculation

Lets say, <br>
EST<sub>t</sub> = current estimate <br>
EST<sub>t-1</sub> = previous estimate <br>
MES = Measurement <br>
then, 

EST<sub>t</sub> = EST<sub>t-1</sub> + KG[MEA - EST<sub>t-1</sub>]

Higher the KG, higher the E<sub>est</sub> and lower the E<sub>mea</sub> <br>
Lower the KG, lower the E<sub>est</sub> and higher the E<sub>mea</sub>

So, by looking at the above proportions, it should make sense to understand that, over the time, the KG should get smaller and smaller as our estimates will keep getting better, the error in data (measurement) being constant.

#### Error in the Estimate Calculation

E<sub>est_t</sub> = ( E<sub>mea</sub> * E<sub>est_t-1</sub> ) / (E<sub>mea</sub> + E<sub>estP_t-1</sub>)

Sometimes, the above eq<sup>n</sup> can also be written as, <br>
E<sub>est_t</sub> = (1 - KG)(E<sub>est_t-1</sub>)

With the above eq<sup>ns</sup>, we can definitely say that the error in the estimates will always get smaller. 
