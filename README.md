# GithubSearch
GithubSearch is a console program to retrieve statistics for Github repositories.

* You will be prompted to enter a project name or a repository url.
* The program will use the Github REST API to:
    * Return the top 10 matching repositories
    * Return each of the top 10 repositories' Language, Number of Contributors, Number of Watchers, Total Stars, Issues, and Number of Forks


Notes:

* It does not have error handling, and certain requests may cause errors.
* It does these operations without any authentication or a Github API Token, and there is a limit to the number of unauthenticated Github API requests per day (once you go over the limit, you will not see any results and will encounter an unhandled Python error message).
