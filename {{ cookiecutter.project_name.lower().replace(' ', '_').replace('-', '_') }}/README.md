# {{ cookiecutter.project_name.title().replace('_', ' ').replace('-', ' ') }}

---

<div align="center">

[![Build status](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/workflows/build/badge.svg?branch=master&event=push)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/releases)
[![License](https://img.shields.io/github/license/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }})](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

{{ cookiecutter.project_description }}

</div>

---

## Features

## Installation

```bash
pip install {{ cookiecutter.project_name }}
```

{% if cookiecutter.create_example_template == 'cli' -%}Then you can run

```bash
{{ cookiecutter.project_name }} --help
```

{%- endif %}

## Usage

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/releases) page.

## 🛡 License

[![License](https://img.shields.io/github/license/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }})](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/LICENSE)

This project is licensed under the terms of the `{{ cookiecutter.license }}` license. See [LICENSE](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/LICENSE) for more details.
