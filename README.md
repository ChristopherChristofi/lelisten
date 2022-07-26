# loglistener
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

Set up a project with Google cloud and Gmail API enabled, to gain API:S credentials.

```sh
pip install -r requirements.txt
```

## Dev/Quickstart:

Still in development.
Generates process for build environment variables, that refer to:
- sender email address
- recipient email address
- email message
- subject.

```sh
python3 loglistener.py --build / -b
```

The above command will build the .env file (current default naming='.loglistenerproject.env') in your home directory.

```sh
python3 loglistener.py --run / -r
```

The above command will instantiate the email service and message send service using the provided environment variables.
The path of the .env variable can be set with the [ --path / -p ] option.

```sh
python3 loglistener.py -brp /<set>/<path>/<relative>/<to>/<home>
```

Above command demonstrates build, send message service and environment path setting (remove --build/-b and this could be a read option of an already .env file in a predetermined file location).

To complete for full functionality
