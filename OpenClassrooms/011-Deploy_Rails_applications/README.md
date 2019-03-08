# Deploy Rails Applications


## Introduction

We've learned how to code some stuff in Ruby, and how to build an application using Rails. It is now time to **deploy** this application in production, typically on the Internet, and make it robust enough to traffic.

The course deploys the app on an AWS server. It happens that AWS requires valid pament information to confirm the account, even for free accounts, and I won't do that now. I therefore **couldn't deploy it on AWS**, which is kinda the whole point of the course.

Hence I cannot validate this course. I will take note of all of the steps below, for the future, and hope that the situation will be resolved one way or another.


<br>


## Part 1 - Putting your application on the Internet

### Preliminary setup

* Create a Rails app
* Initialize a Git repo to handle versioning
* Setup an AWS account - we will be using Elastic Beanstalk (EB)
* Install the EB Command Line Interface (CLI)
* Have an SSH keypair to securely control the servers


### Initialize Elastic Beanstalk

* Make sure `eb` is installed using `eb --version`
* Initialize the EB configuration using `eb init`. This requires AWS IDs.
* Set up a *production* environment using `eb create production`. This makes EB create the server in a virtual machine, and configure it to use all the right software for our Rails app.
* Check the status of your new server using `eb status`. This will also give you the public address of the server, in `CNAME`.
* From now on, when the server is up it can be accessed using `eb ssh`.


### Manage the app

* Rails uses a secret key to encrypt identifying information in the HTTP cookie header being sent between your application and your users' browsers. We don't want this secret key to be stored in clear text; hence it's best to **keep this kind of keys out of the code base, and manage them manually on the remote servers**. We can do this by setting environment variables, here: `eb setenv SECRET_KEY_BASE=$(rails secret)`
* Any change on the app can be deployed following a simple structure:
  1. Make the change in the code
  2. Commit it on Git (not mandatory, but good practice)
  3. Deploy it on the servers using `eb deploy`


<br><br>


## Part 2 - Use Postgres, a production-grade database

* Make sure you have the `pg` gem installed.
* Override the *production* settings in the `database.yml` configuration file. The naive idea would be to simply replace sqlite3 with postgresql, and that's it. This would mean the app comes with its database. However, we typically want multiple instances of our app to run at the same time (to simultaneously process multiple user queries). For the consistency of the data, it is thus preferable to put the database on a separate machine and set up connections. AWS has a service called RDS that manages that; the corresponding parameters are stored in environment variables, and this is what we need to fetch in the config file.
* Setup a RDS instance (AWS online console), and re-deploy the app.<br><br>
* Seed the database in `db/seeds.rb` (i.e. create dummy instances of the models, so that everything appears as expected). Things like passwords, which shouldn't be stored as clear text, should be manually set as environment variables.
* To run the seed scripts on the server, first connect to it using a SSH tunnel (`ssh -i path_to_key ec2_user@public_dns_found_in_ec2_dashboard`), and then simply run the seed scripts using `bin/rails db:seed`. Use your browser to check that the dummy data has been added.<br><br>
* To use Postgres in the development and test environments as well, set it up on your machine and modify the `database.yml` file, setting *postgresql* as default. Then run `rails db:setup` to initialize the correct databases with our models (and the seed data).


<br><br>


## Part 3 - Handle background jobs

### Send email with a background job

* Many production apps have tasks that they'd rather process in the background; otherwise the user may have to wait for the query to finish before seeing another page, which can be pretty long. Background jobs can also help with the performance of the servers.
* Rails allows you to define background jobs using `ActiveJob`, but it needs some additional infrastructure: a database to store our list of jobs (we'll use **Redis**), and a *background server* (just programs, not physical) that will run the jobs in the background (we'll use **Sidekiq**).
* Let's first design a simple background job using Rails' API: sending an email when someone fills out the contact form.
  1. Create a contact form (`rails generate controller contact` > define *new* and *create* actions > add routes for these two actions > create the form HTML in a view template).
  2. Generate the background job *contact* using `bin/rails generate job contact`
  3. Generate an email template and mailer using `bin/rails generate mailer ContactMailer`
  4. Ask our `ContactJob` to send a `ContactEmail` using the `perform` method (have it call `ContactMailer.submission(message).deliver`)
  5. Finally, create the job inside the contact controller, using the method `ContactJob.perform_later`, which is like `perform` but executed later, by another server.


### Set up Redis and Sidekiq locally

* Redis follows a *key-value* storage, much like a hash table. Set it up on your local machine (e.g. using `apt install redis-server` + some configuration work).
* Add the `sidekiq` gem, install it, and tell Rails to use Sidekiq as the queue adapter: in `config/application.rb`, set `config.active_job.queue_adapter = :sidekiq`
* Start the sidekiq server using `bundle exec sidekiq` and reload your server.


### Set up Redis and Sidekiq on your production servers

* Create a machine in AWS (online console) to run our Redis instance (much like we did with Postgres)
* Configure some stuff in the EC2 console (adding a *custom TCP* rule for our Redis instance's security group).<br><br>
* Add the Sidekiq config file in our app (`config/initializers/sidekiq.rb`), which will tell Sidekiq where to find Redis.
* Add `config/redis.yml` that will set, for each environment, the host and the port to connect to Redis.


### Configure Elastic Beanstalk to run Sidekiq

* To run Sidekiq locally, we ran `bundle exec sidekiq`. We need a way to have EB do that for us automatically on the server when we deploy.
* This can be done using **platform hooks**. "Basically, if you put scripts in a special directory located at `/opt/elasticbeanstalk/hooks/` on your servers, Elastic Beanstalk will run them at certain moments during the deploy process. The names of the subdirectories/sub-folders where you place these scripts tells Elastic Beanstalk when to run them." The sub-folders are `appdeploy`, `configdeploy`, `restartappserver`, `preinit`, and `postinit`, and substructure is available too.<br><br>
* We hence want to place a Sidekiq startup script in a predeploy-hook. We could set it manually using SSH, but we want this file to exist every time we create a new application instance, so that's not an option.
* Fortunately, EB gives us a place for scripts we want to run when it creates new instances for us (`./.ebextensions`). We only have to put there a `0002_sidekiq.config` file that will generate the desired hooks.
* Finally, deploy and enjoy!