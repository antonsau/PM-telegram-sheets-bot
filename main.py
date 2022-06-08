import json
import logging
import schedule
import time
import threading
import emoji

import telebot
import spreadsheet as pipeline


# Load config parameters
with open('config.json') as config:
    CONFIG = json.load(config)

# Set variables
bot = telebot.TeleBot(CONFIG['BOT_ID'])
eligible_senders = CONFIG['SENDERS'].split(',')
chat_id = str(CONFIG['INTERNAL_CHATID'])

# Logging
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


@bot.channel_post_handler(content_types=["text", "sticker", "video", "video_note",
                                         "pinned_message", "photo", "audio", "file",
                                         "document", "animation"])
def handle_text_messages(message):
    text = message.caption if (message.text is None) else message.text
    if text.find("FromTheTeam") != -1:
        # Chill
        pass

    pipeline.add_new_message(message)
    # TODO: add reaction to the message (robot emoji)
    # bot.reply_to(message, emoji.emojize("Added, thanks."))
    # Send message to the internal chat
    bot.send_message(chat_id=chat_id,
                     text="Добавлен новый проект.")
    pass


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, mate.")


def schedule_checker():
    while True:
        schedule.run_pending()
        print("All pending tasks completed, sleep.")
        time.sleep(600)


def timesheet_daily_reminder():
    return bot.send_message(chat_id, emoji.emojize(':warning:') +
                            " Всем привет! Не забудьте заполнить/обновить таймшит. Хорошего дня!")


def timesheet_weekly_reminder():
    return bot.send_message(chat_id, emoji.emojize(':warning:') +
                            " Не забудьте заполнить/обновить таймшит на следующую неделю.")


def main():
    # Create jobs in the schedule
    schedule.every().friday.at("12:00").do(timesheet_weekly_reminder)
    schedule.every().monday.at("07:00").do(timesheet_daily_reminder)
    schedule.every().tuesday.at("07:00").do(timesheet_daily_reminder)
    schedule.every().wednesday.at("07:00").do(timesheet_daily_reminder)
    schedule.every().thursday.at("07:00").do(timesheet_daily_reminder)
    schedule.every().friday.at("07:00").do(timesheet_daily_reminder)

    # Create a separate thread
    threading.Thread(target=schedule_checker).start()
    # Run the bot
    bot.infinity_polling()


if __name__ == '__main__':
    main()
