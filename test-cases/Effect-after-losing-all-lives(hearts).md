# Effect after losing all lives (hearts)

## The test will check what will happen if we perform 5 tasks incorrectly and therefore lose 5 chances (hearts/lives).

Enviroment: Production

https://www.duolingo.com/

# Preconditions:

* Logged in user
* Selected course
* Selected available lesson
* Start the lesson by clicking the "START" button
* 5 lives (hearts)

## Steps

|   | Action                                                                  | Input | Expected Result                                                                                  |
|---|-------------------------------------------------------------------------|-------|--------------------------------------------------------------------------------------------------|
| 1 | Start the lesson.                                                       |       | The user sees the first task.                                                                    |
| 2 | Do the exercise incorrect.                                              |       | A message appears informing about the incorrect execution of the task.                           |
|   |                                                                         |       | The `CONTINUE` button appears.                                                                   |
| 3 | Click the `CONTINUE` button.                                            |       | A new exercise appears.                                                                          |
| 4 | Do the exercise incorrectly and continue until you lose all your lives. |       | A modal window appears with the message `You run out of hearts` with a `REFILL FOR FREE` button. |