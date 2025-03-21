requires <https://python-poetry.org/>(poetry) to run

also requires .env file containing
HEURIST_API=heurist api key

to start:
poetry install && poetry run uvicorn node_multiplexer.main:app
