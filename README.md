# django-rmp-data

A Django app to extract, refine and publish Risk Management Plan (RMP) data collected by the U.S. Federal Environment Protection Agency.

## Dependencies

Requires [PostgreSQL](https://www.postgresql.org/), because our ETL process relies heavily on [`django-postgres-copy`](https://django-postgres-copy.readthedocs.io/en/latest/).

Python-related dependencies for this project are managed via [pipenv](https://pipenv.readthedocs.io/en/latest/).

## Bootstrapping a (macOS) local development environment:

Below are the steps to set up a local development on a Mac computer.

Open your terminal application, and type in each of these commands in the order specified.

### 1. Install Xcode Command Line Tools

Xcode is a large suite of software development tools and libraries, provided by Apple. We only need some of these tools (e.g., the GCC compiler), which is included in the subset Xcode called the Command Line Tools:

```bash
xcode-select --install
```

This will take a minute.

### 2. Install Homebrew

Homebrew is an un-official package manager for macOS. It helps us install and configure software that you can't find on the App Store.

You may already have it installed. Let's check by updating to the latest version:

```bash
brew update
```

If you get get something like this:

```bash
Updated Homebrew from bb038c7048 to ff3cede96f.
Updated 2 taps (homebrew/core, homebrew/cask).
==> New Formulae
i2pd                                      opensubdiv                                tdlib
==> Updated Formulae
cgal ✔                                    go                                        logstash
cmake ✔                                   godep                                     mariadb
```

But if you get this:

```bash
brew: command not found
```

Then you need to install it like this:

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 3. Install pyenv

[`pyenv`](https://github.com/pyenv/pyenv) helps you manage different versions of Python running on the same machine.

We can install it with homebrew:

```bash
brew install pyenv
```

### 4. Initialize pyenv in your shell

The default Unix shell for macOS is bash. Here is how we can confirm that this default is still intact:

```bash
echo "$SHELL"
```

And here is what you should see:

```bash
/bin/bash
```

To initialize pyenv, we need to add a few lines of code to a file named `.bash_profile`, which is a configuration file that runs whenever a user starts their shell environment.

According to pyenv's docs:

> Please make sure eval `"$(pyenv init -)"` is placed toward the end of the shell configuration file since it manipulates PATH during the initialization.

Add they provide a handy one-liner for doing exactly that:

```bash
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
```

In order for this change to take effect, restart your shell.

```bash
exec "$SHELL"
```

TODO: This changes the command line prompt? Should we instead to `source .bash_profile`?

### 5. Install recommended Python dependencies

Now we install six additional dependencies for Python, [recommended](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) by pyenv.

```bash
brew install openssl readline sqlite3 xz zlib
```

TODO: Should this step come before `brew install pyenv`?

### 6. Install PostgreSQL

PostgreSQL is an open-source relational database manager, which is required for this project.

```bash
brew install postgresql
```

Then we use a shortcut provided by homebrew for starting PostgreSQL.

```bash
brew services start postgresql
```

### 7. Configure PostgreSQL

We have to create a database for our user profile:

```bash
createdb `whoami`
```

Then create a super user named "postgres", which is the typical configuration.

```bash
createuser -s postgres
```

### 8. Install pipenv

`pipenv` has recently gained a lot of traction as tool to help Python developers manage workflows related to virtual environments, package installation and dependency management. As suchh, it is now the tool [recommended](https://packaging.python.org/tutorials/managing-dependencies/#installing-pipenv) by python.org for managing application dependencies.

```bash
brew install pipenv
```

### 9. Fork our repo



### 10. Clone your fork of the repo

This will create a local copy of project directory in your present working directory.

```bash
git clone https://github.com/[your-github-account-name-here]/django-rmp-data.git
```

### 11. Set up and run your project environment

Navigate into the project folder:

```bash
cd django-rmp-data/
```

Run this script to create a `.env` file where you'll keep secrets, such as database credentials.

```bash
make env
```

TODO: Add this makefile

Then, use `pipenv` to set up your virtual environment and install all necessary dependencies (including the correct version of Python and Django):

```bash
pipenv install
```

Unless you already have Python 3.6 installed, you will get a prompt like this:

```bash
Warning: Python 3.6 was not found on your system...
Would you like us to install CPython 3.6.6 with pyenv [Y/N]:
```
Then you type `Y` and hit enter.

TODO: This step did NOT complete because of an breaking issue between pip and pipenv. We'll let the big guns try to solve this and try again later. If it's still not working, there appears to be a work-around: Pin pip to an early release: <https://github.com/pypa/pipenv/issues/2924>

After all of the project dependencies are instally, you can initiate your virtual environment:

```bash
pipenv shell
```

### 12. Set up the database

We need to create a database on our local PostgreSQL server:

```bash
createdb rmp
```

Then create all of the database tables:

```bash
python manage.py migrate
```

### 13. Import the data

TODO: Figure out how we're going to share the starter data and what the exact commands will be:

```bash
python manage.py import
```

### 14. Start the Django server

At long last, we are ready to start the Django server:

```bash
python manage.py runserver
```

Open you favorite web browser and go to <http://127.0.0.1:8000/> to see our homepage.
