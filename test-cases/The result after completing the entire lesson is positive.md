# The result after completing the entire lesson is positive.

## The purpose of this test case is to check the correct course of the educational process in this application, and in particular the effect of the user completing the entire lesson correctly.

Enviroment: Production

https://www.duolingo.com/ 

## Preconditions:
* Logged in user
* Selected course
* Selected available lesson
* Start the lesson by clicking the 'START' button
* Supply of at least 1 life (hearts)

# Steps

|| Action | Input | Expected Result |
|----|--------|-------|-----------------|
|1|Complete the first task correctly.|| |Green feedback appears indicating that the task has been successfully completed.|
|||| |The `CONTINUE` button appears.|
|2|Click the `CONTINUE` button.|| |Redirects the user to the next task.|
|3|Complete all tasks correctly.|| |The message appears: `Lesson complete`.|
|||| |A short animation appears.|
|||| |There is feedback about the amount of XP collected and whether the user made any mistakes.|
|||| |The `CONTINUE` and `REVIEW LESSON` buttons appear.|
