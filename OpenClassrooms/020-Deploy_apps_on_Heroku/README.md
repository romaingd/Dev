# Deploy apps on Heroku


## Introduction

Heroku is a cloud platform that allows users to deploy multiple applications onto their platform. It aims to be scalable, and is compatible with many languages of modern applications, including Java, Ruby, PHP and Node.

Heroku uses Git as its basis; in essence, creating an app on Heroku is much like creating a remote Git repository, and deploying changes or new versions works much like `git push`. Let's see all that.

<br>


## Deploy a Ruby on Rails applications with Heroku

1. Create a user account for Heroku (with the same email as used in your local Git repo, that you can get with `git config --get user.mail` if it's already configured).
2. Install the Heroku Command Line Interface (CLI), and log in to it using `heroku login` and your Heroku credentials.
3. Make sure you're using:
   * Ruby >= 2.20 (`ruby -v`)
   * Rails >= 5.0 (`rails -v`)
4. Make sure you're using Postgres as your database:
   * In the Gemfile, use `gem pg` instead of `gem sqlite3`
   * In `config/database.yml`, set the adapters to `postgresql`
5. Run `bundle install` to generate a new `Gemfile.lock` and re-install your dependencies if needed
6. Make sure you have Git installed (`git --help`)
7. Navigate to your application inside of the CLI
8. Initiate Git and make a first commit:
   1.  `git init`
   2.  `git add`
   3.  `git commit -m "Initial commit"`
   4.  `git status`
9. Deploy:
   1.  `heroku create`
   2.  `git push heroku master`
   3.  `heroku run rake db:migrate`
10. Visit your site:
    1.  `heroku ps:scale web=1`
    2.  `heroku open`

<br>

Pro tips:
* To push newer code modifications to your Heroku site, repeat steps 6 to 10.
* You can run the Rails console on Heroku using `heroku run rails console`