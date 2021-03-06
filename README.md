# The_Doe_Agency

[![django](https://img.shields.io/badge/Django-v3.2-%23092E20?style=flat-square&logo=django)](https://www.djangoproject.com)
[![python](https://img.shields.io/badge/Python-v3.9-%233776AB?style=flat-square&logo=python)](https://www.python.org)
[![psql](https://img.shields.io/badge/postgresql-13.3-%234169E1?style=flat-square&logo=postgresql)](https://www.postgresql.org)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square&logo=stylelint)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/ziibii88/The_Doe_Agency/branch/main/graph/badge.svg?token=IzFdh1NYXS)](https://codecov.io/gh/ziibii88/The_Doe_Agency)
[![actions](https://github.com/ziibii88/The_Doe_Agency/workflows/TDA_CI/badge.svg)](https://github.com/ziibii88/The_Doe_Agency/actions)
[![CodeQL](https://github.com/ziibii88/The_Doe_Agency/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/ziibii88/The_Doe_Agency/actions/workflows/codeql-analysis.yml)

An agency by John and Jane Doe providing proxy lists to the unknowns

## How to setup development environment
#### (requires Docker to be already installed)
- Step 1 --- Copy `.dev-envs` from `envs` folder to project root (beside `Dockerfile`), save as `.env`
- Step 2 --- Edit `.env` file and add a random `SECRET_KEY`
- Step 3 --- Build the containers `docker-compose build`
- Step 4 --- Run the containers `docker-compose up`
- Step 5 --- You can access api endpoints at `127.0.0.1:8000/api/`
- Step 6 --- You can stop and remove containers by doing `docker-compose down`
