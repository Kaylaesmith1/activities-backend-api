Return to [README](README.md)

# **Iowa Summer Activities API | Testing**


## Table of Contents

* [**Testing**](<#testing>)
    * [Code Validation](<#code-validation>)
    * [Automatic Testing](<#automatic-testing>)
    * [Manual Testing](<#manual-testing>)
    * [Known Bugs](<#known-bugs>)

## Code Validation 

### PEP8

Python codes used throughout the Iowa Summer Activities API were validated using [CI Python Linter](https://pep8ci.herokuapp.com/). 

The most common errors that arose were 'line too long'. This was rectified by adding '  # noqa' to the lines of code in question, which fixed this error.  Please see the results of each component below.

### activities_backend_api files

<details>
  <summary>permissions.py - No errors</summary> 

![Python Validation](images/testing/permissions.png)
</details>
<details>
  <summary>serializers.py - No errors</summary> 

![Python Validation](images/testing/serializers.png)
</details>
<details>
  <summary>settings.py - No errors</summary> 

![Python Validation](images/testing/settings.png)
</details>
<details>
  <summary>urls.py - No errors</summary> 

![Python Validation](images/testing/urls.png)
</details> 
<details>
  <summary>views.py - No errors</summary> 

![Python Validation](images/testing/views.png)
</details>


### Comments App files

<details>
  <summary>models.py - No errors</summary> 

![Python Validation](images/testing/comments-models.png)
</details>
<details>
  <summary>serializers.py - No errors</summary> 

![Python Validation](images/testing/comments-serializers.png)
</details>
<details>
  <summary>urls.py - No errors</summary> 

![Python Validation](images/testing/comments-urls.png)
</details>
<details>
  <summary>views.py - No errors</summary> 

![Python Validation](images/testing/comments-views.png)
</details> 


### Contact App files

<details>
  <summary>models.py - No errors</summary> 

![Python Validation](images/testing/contact-models.png)
</details>
<details>
  <summary>serializers.py - No errors</summary> 

![Python Validation](images/testing/contact-serializers.png)
</details>
<details>
  <summary>urls.py - No errors</summary> 

![Python Validation](images/testing/contact-urls.png)
</details>
<details>
  <summary>views.py - No errors</summary> 

![Python Validation](images/testing/contact-views.png)
</details> 

### Followers App files

<details>
  <summary>models.py - No errors</summary> 

![Python Validation](images/testing/followers-models.png)
</details>
<details>
  <summary>serializers.py - No errors</summary> 

![Python Validation](images/testing/followers-serializers.png)
</details>
<details>
  <summary>urls.py - No errors</summary> 

![Python Validation](images/testing/followers-urls.png)
</details>
<details>
  <summary>views.py - No errors</summary> 

![Python Validation](images/testing/followers-views.png)
</details> 

### Likes App files

<details>
  <summary>models.py - No errors</summary> 

![Python Validation](images/testing/likes-models.png)
</details>
<details>
  <summary>serializers.py - No errors</summary> 

![Python Validation](images/testing/likes-serializers.png)
</details>
<details>
  <summary>urls.py - No errors</summary> 

![Python Validation](images/testing/likes-urls.png)
</details>
<details>
  <summary>views.py - No errors</summary> 

![Python Validation](images/testing/likes-views.png)
</details> 

### Posts App files

<details>
  <summary>models.py - No errors</summary> 

![Python Validation](images/testing/posts-models.png)
</details>
<details>
  <summary>serializers.py - No errors</summary> 

![Python Validation](images/testing/posts-serializers.png)
</details>
<details>
  <summary>urls.py - No errors</summary> 

![Python Validation](images/testing/posts-urls.png)
</details>
<details>
  <summary>views.py - No errors</summary> 

![Python Validation](images/testing/posts-views.png)
</details>

### Profiles App files

<details>
  <summary>models.py - No errors</summary> 

![Python Validation](images/testing/profiles-models.png)
</details>
<details>
  <summary>serializers.py - No errors</summary> 

![Python Validation](images/testing/profiles-serializers.png)
</details>
<details>
  <summary>urls.py - No errors</summary> 

![Python Validation](images/testing/profiles-urls.png)
</details>
<details>
  <summary>views.py - No errors</summary> 

![Python Validation](images/testing/profiles-views.png)
</details>

### Reviews App files

<details>
  <summary>models.py - No errors</summary> 

![Python Validation](images/testing/reviews-models.png)
</details>
<details>
  <summary>serializers.py - No errors</summary> 

![Python Validation](images/testing/reviews-serializers.png)
</details>
<details>
  <summary>urls.py - No errors</summary> 

![Python Validation](images/testing/reviews-urls.png)
</details>
<details>
  <summary>views.py - No errors</summary> 

![Python Validation](images/testing/reviews-views.png)
</details>

## Manual Testing

<!--As well as the automatic tests which can be found in each app's testing.py file, I carried out the following additional manual tests:

| Status | **Profiles**
|:-------:|:--------|
| &check; | Profile List can be ordered by events_count in ascending order
| &check; | Profile List can be ordered by events_count in descending order
| &check; | Profile List can be ordered by followers_count in ascending order
| &check; | Profile List can be ordered by followers_count in descending order
| &check; | Profile List can be ordered by following_count in ascending order
| &check; | Profile List can be ordered by following_count in descending order
| &check; | Profile List can be ordered by going_count in ascending order
| &check; | Profile List can be ordered by going_count in descending order
| &check; | Profile List can be ordered by owner__following__created_at in ascending order
| &check; | Profile List can be ordered by owner__following__created_at in descending order
| &check; | Profile List can be ordered by owner__followed__created_at in ascending order
| &check; | Profile List can be ordered by owner__followed__created_at in descending order
| &check; | Profile List can be filtered by owner__following__followed__profile
| &check; | Profile List can be filtered by owner__followed__owner__profile

| Status | **Events**
|:-------:|:--------|
| &check; | Event List can be ordered by comments_count in ascending order
| &check; | Event List can be ordered by comments_count in descending order
| &check; | Event List can be ordered by interested_count in ascending order
| &check; | Event List can be ordered by interested_count in descending order
| &check; | Event List can be ordered by going_count in ascending order
| &check; | Event List can be ordered by going_count in descending order
| &check; | Event List can be ordered by review_count in ascending order
| &check; | Event List can be ordered by review_count in descending order
| &check; | Event List can be ordered by average_rating in ascending order
| &check; | Event List can be ordered by average_rating in descending order
| &check; | Event List can be ordered by interested__created_at in ascending order
| &check; | Event List can be ordered by interested__created_at in descending order
| &check; | Event List can be ordered by going__created_at in ascending order
| &check; | Event List can be ordered by going__created_at in descending order
| &check; | Event List can be ordered by event_date in ascending order
| &check; | Event List can be ordered by event_date in descending order
| &check; | Event List can be searched on by owner 'admin'
| &check; | Event List can be searched on by title 'event'
| &check; | Event List can be searched on by tag 'sport'
| &check; | Event List can be searched on by event_date '18'
| &check; | Event List can be searched on by event_date '04' for all April events
| &check; | Event List can be filtered by owner__followed__owner__profile
| &check; | Event List can be filtered by interested__owner__profile
| &check; | Event List can be filtered by going__owner__profile
| &check; | Event List can be filtered by owner__profile
| &check; | Event List can be filtered by category

| Status | **Comments**
|:-------:|:--------|
| &check; | Comment List can be filtered by event

| Status | **Reviews**
|:-------:|:--------|
| &check; | Review List can be filtered by event

| Status | **Contact**
|:-------:|:--------|
| &check; | Logged in user can create a contact message


## Known Bugs

### Resolved

1. In my first project inception mentor meeting, I asked about what kind of field a 'Tags' model field would be, and whether it could just be a standard CharField. My mentor said that keywords should be stored in an array, so after further investigation I installed the Django Taggit Manager package to create an automatic array of words the user inputs into the events form 'tags' field. For some reason, however, despite using the blank=True attribute as per the Taggit docs, the API still requires this field to be filled in in order to sucessfully create a new event. I decided that this was not the end of the world and after a lot of research I left it as a required field. When I came to testing, my events tests were failing since I had changed over to Taggit, and so I had to amend the tests where an event is created to include a tags field as well as the title in order for the tests to pass. 

2. While testing the followers app, the test 'can_view_follower_list' kept failing and I couldn't understand why. I tried using the model field names for owner and followed but this didn't work. I tried using the related field names but this didn't work either. In the end, I realised while trying to replicate the process in the local server, the URL for Profile List was different. It was missing the last '/' so I amended this in the urls.py file and all the tests passed after this. 

3. Setting up the tests for the contact app, I can't seem to create the test correctly for 'logged_out_user_can_create_contact' and 'logged_in_user_can_create_contact'.  I don't seem to be setting up the create object response correctly, and I asked tutor support and they were unable to tell me how to do it correctly. I decided to do manual tests on this app until I could seek further advice, and on beginning the manual testing, I found that my permsisions were not set up correctly, and I could in fact create a contact whilst being logged out, hence why my automatic test was failing. I have now changed the permissions, and the automatic test for 'logged_out_user_cant_create_contact is now passing. 

![Contact Test Fail](images/fail_create_contact_test.png)

Please click [**_here_**](README.md) to return to the Happening API README file. -->