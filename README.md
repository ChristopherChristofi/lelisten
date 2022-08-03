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

Set up a project with Google cloud and Gmail API enabled, to gain API access credentials (*client secrets*.json).

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
- subject
- filename for clients secrets

```sh
lelisten -b
```

The above command will build both the .lelisten directory and contained .lelisten.env file within your home directory. Place your Gmail api secrets in the created .lelisten directory (default naming='google_client_secret.json', path is saved to the .lelisten.env, naming can be set with --build/-b command or written directly in the .lelisten.env file).

```sh
lelisten -r
```

The above command will instantiate the email service and message send service using the provided environment variables. Without the --build/-b, this could be a read option of an already existing .lelisten.env file in the .lelisten directory of your home folder.

For more information:

```sh
lelisten --info
```

To complete for full functionality
