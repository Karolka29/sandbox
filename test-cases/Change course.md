# Changing the Language Course from the Current One to Another.

## The test aims to evaluate the effectiveness of the application's user interface in handling language changes, ensuring the process is intuitive and efficient for the user.

Enviroment: Production

https://www.duolingo.com

## Preconditions:
* Logged in user
* At least 2 language courses selected
* Main page view

## Steps

|| Action | Input | Expected Result |
|----|--------|-------|-----------------|
|1||Hover over the flag icon (visible on the right panel).||||The `MY COURSES` submenu expands.|
|2||Click on the icon of a language different from the current one.||||The URL changes to https://www.duolingo.com/learn|
|||||||Redirects the user to the main page for the selected language (the page with lessons).|