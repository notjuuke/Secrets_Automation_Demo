# How to set up Secrets Automation in a Local Environment (Mac)

## 1. Install Docker macOS app 
1. Download and install the [Docker Desktop app](https://www.docker.com/products/docker-desktop)

### Verify Docker installation
1. Open a terminal and enter `docker run -d -p 80:80 docker/getting-started via terminal`
2. Open the Docker app, locate `docker/getting-started`, and click the "Open in Browser" button: 

![Screenshot](https://user-images.githubusercontent.com/34498957/121909827-4d8f6480-ccfc-11eb-8950-30c1164fb4ce.png)

This will open your default browser. You should be presented with the Docker's Getting Started documentation.

1. Open your terminal and enter `docker-compose version`. You should see something like `Docker Compose version 2.0.0`. 

## 3. Create a Secrets Automation Integration on 1Password.com

1. [Sign in](https://start.1password.com/signin?l=en) to your account on 1Password.com.
2. Click `Integrations` in the sidebar, then choose **Secrets Automation**.
3. Choose an Environment name.
4. Click `Choose Vaults` > [your desired vault]
   1. **Note:** You need to select a user created vault. You cannot use one of the default 1password vaults (Private or Shared).
5. Enter your token name and desired expiration parameter. 
6. Click `Choose Vaults` and select the same vault that you did in step 4.
7. Click `Issue Token`.
8. Save **both** your `Credentials File` and `Access Token` in 1Password. 

## 4. Set up your local environment

1. Create a folder to store all of your project files. 
2. Download your `1password-credentials.json` file and move it into your project folder.
3. Download this [sample docker-compose file](https://i.1password.com/media/1password-connect/docker-compose.yaml) and move it into your project folder.

## 5. Start your Docker containers

1. Open a terminal and navigate to your project folder. Ex: `cd Documents/Secrets_Automation/`
   1. This example assumes your project folder is naemd `Secrets_Automation` and was created in your `Documents` folder.
2. In your terminal, enter `docker compose up -d`.

You're ready to [set up your apps / services to securely retreive 1Password data](https://support.1password.com/connect-deploy-docker/#step-3-set-up-applications-and-services-to-get-information-from-1password)!

# Connect API example

## Requirements

- [Python 3](https://www.python.org/downloads/release/python-395/)
- [1Password Connect API](https://support.1password.com/connect-api-reference/)

Our containers are currently running a connect server, but nothing really happens until we make a request via the 1Password Connect API. I've written an example script, `request.py` that you can use to make a request with the 1Password Connect API. You'll want to replace `{Your_1Password_Connect_API_Token}`, `{your_item_id}`, and `{your_vault_id}` with their respective replacements. 

To run this program, navigate to your project folder via a terminal. You can then enter `python3 request.py` to run the script. This script will return two objects: 

- A list of the vault(s) available to your connect sever.
- The details of a specific item you requested.