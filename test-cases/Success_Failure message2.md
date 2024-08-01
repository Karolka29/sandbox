# Application displays a success/failure message after completing a task.

## The test will check the display of success or failure messages after completing a task.

Enviroment: Production

https://www.duolingo.com 

## Preconditions: 
* Logged-in user
* Selected course
* Selected available lesson
* Lesson started by clicking the `START` button
* 5 life (hearts) available

## Steps

|| Action | Input | Expected Result |
|----|--------|-------|-----------------|
|1||Perform the first task correctly.||||A green `CORRECT` message and a `CONTINUE` button appear on the bottom panel.|
|2||Click the `CONTINUE` button.||||Redirects the user to the next task.| 
|3||Perform the task incorrectly.||||A red message appears on the bottom panel, suggesting the correct way to complete the task (`Correct solution: ... `)|
|||||||A `CONTINUE` button appears.|
|||| |User loses one life (one heart per error).|  

