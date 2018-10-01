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

Homebrew is an un-official package manager for macOS. It helps us install and configure software that you can't find on the App Store>

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 3. Install pyenv

[`pyenv`](https://github.com/pyenv/pyenv) helps you manage different versions of Python running on the same machine.

```bash
brew update
brew install pyenv
```

### 4. Configure your shell to use pyenv

Add `pyenv init` to your shell to enable shims and autocompletion. Please make sure eval `"$(pyenv init -)"` is placed toward the end of the shell configuration file since it manipulates PATH during the initialization.

```bash
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
```

In order for this change to take effect, restart your shell.

```bash
exec "$SHELL"
```

### 5. Install recommended Python dependencies

Now we install six additional dependencies for Python, [recommended](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) by pyenv.

```bash
brew install openssl readline sqlite3 xz zlib
```

### 6. Install PostgreSQL

PostgreSQL is an open-source relational database manager, which is required for this project.

```bash
brew install postgresql
```

### 7. Configure PostgreSQL

TODO: Not as certain about this step, but I think the commands are...

```bash
brew services start postgresql
```

```bash
createdb `whoami`
```

```bash
createuser -s postgres
```

### 8. Install pipenv

`pipenv` has recently gained a lot of traction as tool for Python developers manage workflows related to virtual environments, package installation and dependency management. `pipenv` is now the tool [recommended](https://packaging.python.org/tutorials/managing-dependencies/#installing-pipenv) by python.org for managing application dependencies.

```bash
brew install pipenv
```

### 9. Clone the repo

This will create a local copy of project directory in your present working directory.

```bash
git clone https://github.com/rji-futures-lab/django-rmp-data.git
```

### 10. Set up and run your project environment

Navigate into the project folder:

```bash
cd django-rmp-data/
```

Run this script to create a `.env` file where you'll keep secrets, such as database credentials.

```bash
make env
```

TODO: Add this makefile

Then, use `pipenv` to set up your virtual environment, install all necessary dependencies (including the correct version of Python and Django), and initiate your virtual environment:

```bash
pipenv shell
```


### 11. Set up the database

We need to create a database on our local PostgreSQL server:

```bash
createdb rmp
```

Then create all of the database tables:

```bash
python manage.py migrate
```

### 12. Import the data

TODO: Figure out how we're going to share the starter data and what the exact commands will be:

```bash
python manage.py import
```

### 13. Start the Django server

At long last, we are ready to start the Django server:

```bash
python manage.py runserver
```

Open you favorite web browser and go to <http://127.0.0.1:8000/> to see our homepage.
