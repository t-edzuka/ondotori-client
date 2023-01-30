vpy := "venv/bin/python"
vpip := "venv/bin/pip"

# 引数としてそのまま評価する場合はsingle quoteを利用する
source := '"ondotori_client"'

create_venv:
    echo "$(which python)"
    echo "$(python --version)"
    python -m venv venv


update_deps:
	{{vpy}} -m pip install --upgrade pip-tools pip wheel
	{{vpy}} -m piptools compile --upgrade --resolver backtracking -o requirements/main.txt pyproject.toml
	{{vpy}} -m piptools compile --extra dev --upgrade --resolver backtracking -o requirements/dev.txt pyproject.toml


install:
    {{vpy}} -m pip install --upgrade pip wheel
    {{vpy}} -m pip install --upgrade -r requirements/main.txt -r requirements/dev.txt -e "."
    {{vpy}} -m pip check
    pre-commit install



format:
	{{vpy}} -m isort {{source}}
	{{vpy}} -m black {{source}}


lint:
	{{vpy}} -m ruff {{source}}
	{{vpy}} -m isort {{source}} --check-only --df
	{{vpy}} -m black {{source}} --check --diff
