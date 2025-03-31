# Gatekeeper 🔒🚪

This was a fun little personal project I did for myself as I tried to push my limits by trying something new that my server needed at the time.

## Made with ⚙️  

* Nextcord
* Python
* python-dotenv

## Description 📜

Gatekeeper is a custom Discord bot built using the Nextcord library. It serves as a verification bot for Discord servers, ensuring users have two specific roles before granting them the verified role and allowing them full access to the server. This bot continuously monitors user roles for changes to automate the verification process.

## How to Use 🚀

1.  **Prerequisites:**
    * Python 3.7 or higher
    * Nextcord library installed (`pip install nextcord`)
    * `python-dotenv` library installed (`pip install python-dotenv`)

2.  **Setup:**
    * Clone this repository to your local machine or cloud instance.
    * Create a `.env` file in the root directory of the project.
    * Add the following environment variables to the `.env` file, replacing the placeholder values with your actual Discord bot token, guild ID, and the IDs of the two required roles and the verified role:

        ```env
        discord_bot_token = "insert_bot_token_here"
        guild_id = "insert_guild_id_here"
        role1 = "insert_role_id_here"
        role2 = "insert_role_id_here"
        verified_role_id = "insert_role_id_here"
        unverified_role = "insert_role_id_here"
        ```

        **Note:** You will need to obtain your bot token from the Discord Developer Portal and the guild and role IDs from your Discord server.

3.  **Running the Bot:**

    * **Locally:** Open your terminal or command prompt, navigate to the project directory, and run the bot using the following command:

        ```bash
        python Gatekeeper.py
        ```

    * **Cloud Deployment (Recommended):** For continuous 24/7 operation, it is highly recommended to deploy this bot to a cloud hosting platform such as Heroku, AWS, Google Cloud, or similar services (in my case I used Discloud). Follow the platform's specific deployment instructions, ensuring that your `.env` file is properly configured in the cloud environment.

## License 📄

This project is licensed under the [MIT License](LICENSE).

##
Made with ❤️ by Texdroid
