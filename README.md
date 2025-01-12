DO NOT USE IF YOU DONT WANT TO GET BANNED
THIS WAS ONLY FOR FUN
# Instagram Bot

This script automates the process of following users on Instagram by targeting the followers of specified users. It logs activities and handles errors gracefully.

## Features

- **Login Automation:** Logs into Instagram using provided credentials.
- **Follow Followers:** Follows a specified number of followers for each targeted user.
- **Error Handling:** Logs errors during the process for troubleshooting.
- **Delay Management:** Includes delays between actions to avoid being flagged by Instagram.

## Dependencies

- **instabot:** Python library used for automating Instagram actions.

  Install the `instabot` package via pip if it's not already installed:

  ```bash
  pip install instabot

  Replace `username=""` and `password=""` with your Instagram credentials in the script.

## Target Users:

Modify the `users_to_target` list with the Instagram usernames of the users whose followers you want to follow.

## Run the Script:

Execute the script using a Python interpreter.

## Usage

**Function to Follow Followers:**

The `follow_followers_of_user` function fetches followers of the specified user and follows a certain number of them.

## Configuration:

Adjust the `users_to_target` list and `users_to_follow_per_day` variable to fit your needs.

## Logging

The script logs activities and errors to `instagram_bot.log`. This helps in tracking the bot's actions and troubleshooting any issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
