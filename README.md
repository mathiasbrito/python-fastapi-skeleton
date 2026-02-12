# Installing

## Development

For development purposes install this package with pip:

```
pip install -e .
```

You can then run at any time the O1 termination using the command `app`. 

## Testing

Install the test dependencies by running:

```
pip install -r tests/requirements.txt
```

## Running Tests

You can run the tests using `pytest`:

```bash
pytest
```

Or using `tox` to run tests in a clean environment:

```bash
tox
```

## Building and running a docker image

docker build -t my-app .
docker run -p 8000:8000 my-app

