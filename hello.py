from instabot import Bot
import time
import logging

# Set up logging
logging.basicConfig(filename='instagram_bot.log', level=logging.INFO)

# Initialize the bot
bot = Bot()

try:
    # Login to your account
    bot.login(username="", password="")

    # Function to follow users from a user's followers
    def follow_followers_of_user(user, num_to_follow):
        try:
            followers = bot.get_user_followers(user)
            for follower in followers[:num_to_follow]:
                try:
                    bot.follow(follower)
                    logging.info(f"Followed {follower} (follower of {user})")
                except Exception as e:
                    logging.error(f"Error following {follower}: {e}")
                time.sleep(30)  # Delay to avoid being flagged by Instagram
        except Exception as e:
            logging.error(f"Error fetching followers of {user}: {e}")

    # List of users to target
    users_to_target = ["epoxydecorativefloors", "epoxywoodworking", "leggari"]

    users_to_follow_per_day = 50

    # Follow users from each user's followers
    for user in users_to_target:
        follow_followers_of_user(user, users_to_follow_per_day)

except Exception as e:
    logging.error(f"General error: {e}")
finally:
    # Ensure logout even if there's an error
    bot.logout()