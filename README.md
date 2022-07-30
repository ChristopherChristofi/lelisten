# lelisten
email alert service daemon
- still in development

## dev dependencies:

- python-dotenv
- google-auth-httplib2
- google-api-python-client
- google-auth-oauthlib

## Requirements:

- Python 3+

## Installation:

Set up a project with Google cloud and Gmail API enabled, to gain API access credentials (client_secret.json).

```sh
python3 -m venv venv
. venv/bin/activate
pip install --editable .
```

## Dev/Quickstart:

Still in development.

Use build option to generate process for build environment variables, that refer to:
- sender email address
- recipient email address
- email message
- subject.

```sh
lelisten -b
```

The above command will build the .env file (current default naming='.lelisten.env') in your home directory.

```sh
lelisten -r
```

The above command will instantiate the email service and message send service using the provided environment variables.
The path of the .env variable can be set with the [ --path / -p ] option.

```sh
lelisten -brp /<set>/<path>/<relative>/<to>/<home>
```

Above command demonstrates build, send message service and environment path setting (remove --build/-b and this could be a read option of an already .env file in a predetermined file location).

For more information:

```sh
lelisten --info
```

To complete for full functionality
