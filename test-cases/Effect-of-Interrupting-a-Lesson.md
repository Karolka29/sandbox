# Effect of Interrupting a Lesson

## This test will verify what happens when a user quits a lesson while performing tasks.

Environment: Production

https://www.duolingo.com

## Preconditions

* Logged-in user
* Selected course
* Selected available lesson
* Lesson started by clicking the `START` button
* At least 1 life (heart) available

## Steps

|  | Action                                                                                   | Input | Expected Result                                                                                                                                                       |
|--|------------------------------------------------------------------------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Perform at least one task.                                                               |       | The task is done.                                                                                                                                                     |                                                                                                                                                                       |The `CONTINUE` button appears.| 
| 2 | Click the `Close Button` (X) on the left side of the bar displayed above the task content. |       | A modal window with the message `Wait, don’t go! You’ll lose your progress if you quit now` appears, along with the buttons `KEEP LEARNING` and `END SESSION` button. |
| 3 | Click the `END SESSION` button.                                                          |       | Redirects the user to the home page.                                                                                                                                  |
