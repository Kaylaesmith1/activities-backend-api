Return to [README](README.md)

# **Iowa Summer Activities API | Testing**


## Table of Contents

* [**Testing**](<#testing>)
    * [Code Validation](<#code-validation>)
    * [Manual Testing](<#manual-testing>)
    * [Bugs](<#known-bugs>)

## Code Validation 

### PEP8

Python codes used throughout the Iowa Summer Activities API were validated using [CI Python Linter](https://pep8ci.herokuapp.com/). 

The most common errors that arose were 'line too long'. This was rectified by adding '  # noqa' to the lines of code in question, which fixed this error.  Please see the results of each component below.

### Activities_backend_api files

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


#### [Back to top](<#table-of-contents>)

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

#### [Back to top](<#table-of-contents>)

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

#### [Back to top](<#table-of-contents>)


## Manual Testing
I started by ensuring each url path worked properly by running the backend server and manually entering the urls (following the url pathways I have in the activities_backend_api urls.py file). All opened without error.

I then checked CRUD functionality worked properly through the API by logging in as a superuser and testing these features. CRUD functionality should be available for all seven apps: Comments, Contact, Followers, Likes, Posts, Profiles and Reviews.

Once logged in as the superuser, I went through each of the aforementioned apps by url to see if I was able to: create an item, edit an item and delete an item, which I was able to do on all accounts.

I performed manual testing using the Django Rest Framework admin site  throughout the development of this project as a whole. Furthermore, I did manual testing at various steps on the Iowa Summer Activities frontend website, which will be discussed in depth in the TESTING.md file in the frontend documentation.

All API endpoints in this portion of the project pass manual testing by posting, retrieving, updating and deleting data, both through the frontend website as well as through the Django rest framework admin site. 

## Resolved Bug


1. <details>
    <summary>Contact form error</summary> 

    ![Contact form error](images/bugs/contact-form-error.png)
    </details>

    In early development of the Contact model, the form was not posting correctly to the backend API. After troubleshooting on my own and speaking with someone from tutoring, I was reminded I needed to migrate new changes to the model and deploy the backend again. This suggestion solved the problem, errors in the console disappeared and my information from the contact form was posted to the backend correctly. 


## Unresolved Bug
There are no other unresolved bugs that I am aware of. Below is a description of the bug identified.

1. <details>
    <summary>POST / GET errors</summary> 

    ![Contact form error](images/bugs/post-get-errors.png)
    </details>
    
    These errors show up periodically if the user is not logged in from the frontend website. I spoke to Sean from tutoring and he assured me that this is a known issue and it would not count against my assessment (see below). Furthermore, once the user is logged in the errors disappear, though a hard refresh might be needed.

    <details>
    <summary>Sean's response</summary> 

    ![Contact form error](images/bugs/backend-error.png)
    </details>


    #### [Back to top](<#table-of-contents>)
