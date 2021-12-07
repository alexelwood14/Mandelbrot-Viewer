Alex Elwood | June 2020

Zoom In 			       -  W
Zoom Out 			       -  S
Move Up				       -  Up Arrow
Move Down 			       -  Down Arrow
Move Left			       -  Left Arrow
Move Right			       -  Right Arrow
Decrease Mandelbrot Formula Iterations -  R
Increase Mandelbrot Formula Iterations -  F
Terminate Program                      -  Esc

## Movement: ##

accelerateForwards will increase the velocity of the baloon until it is at terminal velocity. 

`accelerateForwards()`

accelerateBackwards will decrease the velocity of the baloon until it is reversing at terminal velocity.

`accelerateBackwards()`

accelerateUp will increase the velocity of the baloon vertically until it is increaseing in altitude at terminal velocity.

`accelerateUp()`

accelerateDown will decrease the velocity of the baloon vertically until it is decreaseing in altitude at terminal velocity.

`accelerateDown()`

accelerateClockwise will increase the rotational velocity of the baloon in the clockwise direction until it is at terminal rotational velocity. 

`accelerateClockwise()`

accelerateAnticlockwise will increase the rotational velocity of the baloon in the anticlockwise direction until it is at terminal rotational velocity. 

`accelerateAnticlockwise()`
 

## Sensors: ##

forwardSensor will get the distance to the nearest object in front of the baloon.

`forwardSensor()`

backwardSensor will get the distance to the nearest object behind the baloon.

`backwardSensor()`

upSensor will get the distance to the nearest object above the baloon.

`upSensor()`

downSensor will get the distance to the nearest object below the baloon.

`downSensor()`

leftSensor will get the distance to the nearest object to the left of the baloon.

`leftSensor()`

rightSensor will get the distance to the nearest object to the right of the baloon.

`rightSensor()`
 
## Getters: ##

getPosition returns the current possition of the baloon.

`getPosition()`

getVelocity returns the current velocity of the baloon as a vector.

`getVelocity()`

getAcceleration returns the current acceleration of the baloon as a vector.

`getAcceleration()`

getRotation returns the current angel of the baloon. [In relation to what???]

`getRotation()`

getRotationalVelocity returns the current rotational velocity of the baloon (positive if turning clockwise).

`getRotationalVelocity()`

getRotationalAcceleration returns the current rotational acceleration of the baloon (positive if turning clockwise).

`getRotationalAcceleration()`

getScore returns the current score.

`getScore()`

