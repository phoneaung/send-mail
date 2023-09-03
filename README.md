# Email Sending Python Program

This Python program allows you to send emails using the Gmail SMTP server. You can use this program to send plain text emails with customizable sender, recipient, subject, and body.

In this project, we import the certifi library to ensure that the program uses a trusted set of root CA certificates. This helps in establishing secure SSL/TLS connections when communicating with the Gmail SMTP server. The certifi bundle provides a collection of up-to-date CA certificates that are recognized by major web services and ensures that your email communication is secure and reliable.

## Table of Contents

- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Requirements

Before using this program, ensure that you have the following prerequisites installed:

- Python 3.x
- The `python-decouple` library (install using `pip install python-decouple`)
- A Gmail account or an Outlook account from which you want to send emails
- The `certifi` library (install using `pip install certifi`) for gmail server.

## Getting Started

### Installation

1. Clone this repository to your local machine:

    ```bash
   git clone https://github.com/phoneaung/send-email.git

2. Navigate to the project directory:

    ```bash
    cd send-email

3. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt

## Usage
Run the Python program:

    python send_email.py

Follow the on-screen prompts to input the sender's email address, recipient's email address, subject, email body, and email password (you can also set the password in a .env file as described in the Configuration section).

The program will send the email using the provided information.

## Configuration
You can configure your email password using a .env file for added security. Here's how:

1. Create a .env file in the project directory.
2. Inside the .env file, add the following line:
EMAIL_PASSWORD=your_email_password_here
Replace your_email_password_here with your actual email password or app password.

The program will read the email password from the .env file when you run it.
