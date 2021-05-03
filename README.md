# Python - Receive A Message Tutorial

This project serves as a guide to help you build an application with FreeClimb. View this tutorial on [FreeClimb.com](https://docs.freeclimb.com/docs/how-to-receive-a-message#section-python). Specifically, the project will:

- Accepts incoming SMS messages and respond to them

## Setting up your new app within your FreeClimb account

To get started using a FreeClimb account, follow the instructions [here](https://docs.freeclimb.com/docs/getting-started-with-freeclimb).

## Setting up the Tutorial

1. Make sure you have Python 3.5.0 or later

2. Install the required packages

    ```bash
    pip install -r requirements.txt
    ```

3. Configure environment variables

   | ENV VARIABLE            | DESCRIPTION                                                                                                                                                                             |
   | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | ACCOUNT_ID              | Account ID which can be found under [API credentials](https://www.freeclimb.com/dashboard/portal/account/authentication) in Dashboard                                                         |
   | API_KEY              | API key which can be found under [API credentials](https://www.freeclimb.com/dashboard/portal/account/authentication) in Dashboard                                               |

## Running the Tutorial

```bash
env FLASK_APP=python_receive_a_message_tutorial.py flask run
```

## Getting Help

If you are experiencing difficulties, [contact support](https://freeclimb.com/support).
