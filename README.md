# msof_api

[![Build Status](https://travis-ci.org/likelion-kookmin/msof_api.svg?branch=master)](https://travis-ci.org/likelion-kookmin/msof_api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

msof. Check out the project's [documentation](http://likelion-kookmin.github.io/msof_api/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)
- pre-commit
    - pip install pre-commit
    - pre-commit install

# Local Development

Start the dev server for local development:
```bash
docker-compose up -d
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
