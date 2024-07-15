# Procurement Benefits

This project is a Django-based web application for managing procurement benefits.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Clone the Repository

First, clone the repository from GitHub:

```sh
git clone https://github.com/sethwhenton/procurement-web.git
cd procurement-web
```

### Set Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies. You can create and activate a virtual environment as follows:

#### On Windows:

```sh
python -m venv venv
venv\Scripts\activate
```

#### On macOS and Linux:

```sh
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

With the virtual environment activated, install the project dependencies using `pip`:

```sh
pip install -r requirements.txt
```

### Apply Migrations

Run the following commands to apply migrations and set up the database:

```sh
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser

Create a superuser to access the Django admin panel:

```sh
python manage.py createsuperuser
```

### Run the Development Server

Finally, run the development server:

```sh
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to access the application.

## Usage

After setting up the project, you can start using the application to manage procurement benefits. Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials created earlier.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

