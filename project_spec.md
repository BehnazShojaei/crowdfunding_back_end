![The She Codes Logo](../../global_images/logo.png)

# Django Rest Framework Project: Crowdfunding App (Part 1)<br><sub><sup><sub>Due: Last Sunday of the module at 11:59pm.</sub></sup></sub>

## Project Description
Kickstarter, Go Fund Me, Kiva, Change.org, Patreon… All of these different websites have something in common: they provide a platform for people to fund projects that they believe in, but they all have a slightly different approach. You are going to create your own crowdfunding website, and put your own spin on it!

## Project Requirements
Your crowdfunding project must:

- [ ] Be separated into two distinct projects: an API built using the Django Rest Framework and a website built using React. 
- [x] Have a cool name, bonus points if it includes a pun and/or missing vowels. See https://namelix.com/ for inspiration. <sup><sup>(Bonus Points are meaningless)</sup></sup>
-  [x] Have a clear target audience.
-  [x] Have user accounts. A user should have at least the following attributes:
  -  [x] Username
  -  [x] Email address
  -  [x] Password
-  [x] Ability to create a “project” to be crowdfunded which will include at least the following attributes:
  -  [x] Title
  -  [x] Owner (a user)
  -  [x] Description
  -  [x] Image
  -  [x] Target amount to fundraise
  -  [x] Whether it is currently open to accepting new supporters or not
  -  [x] When the project was created
-  [x] Ability to “pledge” to a project. A pledge should include at least the following attributes:
  -  [x] An amount
  -  [x] The project the pledge is for
  -  [x] The supporter/user (i.e. who created the pledge)
  -  [x] Whether the pledge is anonymous or not
  -  [x] A comment to go along with the pledge
-  [x] Implement suitable update/delete functionality, e.g. should a project owner be allowed to update a project description?

- **Project**
  - [X] Create, POST
  - [X] Retrieve, GET
  - [X] Update, PUT
  - [ ] Destroy, DELETE - projects cannot be deleted (to avoid issues); however, the owner can close them to prevent further pledges
- **Pledge**
  - [X] Create, POST
  - [X] Retrieve, GET
  - [X] Update, PUT
  - [X] Destroy, DELETE
- **User**
  - [X] Create, POST
  - [X] Retrieve, GET
  - [X] Update, PUT
  - [ ] Destroy, DELETE - users cannot be deleted to maintain system consistency and avoid potential issues

- **UserProfile**
  - [X] Retrieve the list of projects and pledges for each user, GET



---

-  [x] Implement suitable permissions, e.g. who is allowed to delete a pledge?

---

**My permission plan:**
- **Project**
  - [X] ONLY USERS can create new projects
  - [X] ANYONE can retrieve projects
  - [X] ONLY OWNER/ADMIN can edit projects
  
- **Pledge**
  - [X] ONLY USERS can make a pledge
  - [X] ANYONE can get the list of pledges
  - [X] ONLY PLEDGE OWNERS / SUPPORTER can update their pledge

- **User**
  - [X] Limit who can retrieve - user detail view is restricted to the logged-in user
  - [X] Limit who can update
  - [X] Limit who can delete


-  [x] Return the relevant status codes for both successful and unsuccessful requests to the API.

- [X] 200 OK: For successful GET requests.
- [X] 201 Created: For successful POST (creation) requests.
- [X] 404 Not Found: For requests to resources that do not exist.
- [X] 400 Bad Request: For invalid input or data.
- [ ] 204 No Content: For successful DELETE requests. Later it commented out. As decided not to include the DELETE


-  [ ] Handle failed requests gracefully (e.g. you should have a custom 404 page rather than the default error page).
 Will be addressed in front end.
-  [x] Use Token Authentication, including an endpoint to obtain a token along with the current user's details.
-  [ ] Implement responsive design.
Will be addressed in front end.

## Additional Notes
No additional libraries or frameworks, other than what we use in class, are allowed unless approved by the Lead Mentor.

Note that while this is a crowdfunding website, actual money transactions are out of scope for this project.

## Submission
To submit, fill out [this Google form](https://forms.gle/34ymxgPhdT8YXDgF6), including a link to your Github repo. Your lead mentor will respond with any feedback they can offer, and you can approach the mentoring team if you would like help to make improvements based on this feedback!

Please include the following in your readme doc:
- [ ] A link to the deployed project.
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a token being returned.
- [ ] Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
- [ ] Your refined API specification and Database Schema.