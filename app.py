import os

from dotenv import load_dotenv
from slack_bolt import App
from slack_sdk.web import SlackResponse

from model.user_info import User, UserProfile

load_dotenv()

ADMIN_USER = "U06AQJ3J86B"
CHANNEL_ID = "C06JP2Y9GP3"

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.middleware
def log_request(logger, body, next):
    logger.debug(body)
    return next()


@app.error
def global_error_handler(error, body, logger):
    logger.exception(error)
    logger.info(body)


@app.action("deploy-front")
def deploy_front(user_id, ack):
    ack()
    app.client.chat_postMessage(
        channel=CHANNEL_ID,
        blocks=[
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Front",
                    "emoji": True
                }
            }, {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*종류:*\n배포"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*요청자:*\n<@{user_id}>"
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
                        "alt_text": "placeholder"
                    }
                ]
            }
        ]
    )


@app.action("deploy-back")
def deploy_front(user_id, ack):
    ack()
    app.client.chat_postMessage(
        channel=CHANNEL_ID,
        blocks=[
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Back",
                    "emoji": True
                }
            }, {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*종류:*\n배포"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*요청자:*\n<@{user_id}>"
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
                        "alt_text": "placeholder"
                    }
                ]
            }
        ]
    )


@app.action("download-log-back")
def deploy_front(user_id, ack):
    ack()
    app.client.chat_postMessage(
        channel=CHANNEL_ID,
        blocks=[
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Back",
                    "emoji": True
                }
            }, {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*종류:*\n로그"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*요청자:*\n<@{user_id}>"
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
                        "alt_text": "placeholder"
                    }
                ]
            }
        ]
    )


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    response: SlackResponse = app.client.users_info(user=ADMIN_USER)
    user = User(**response.data['user'])
    user_profile = UserProfile(**user.profile)
    submitted_name = f"*{user_profile.real_name}*"
    submitted_image_url = user_profile.image_72

    try:
        client.views_publish(
            user_id=event["user"],
            view={
                "type": "home",
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Rising X Manager",
                            "emoji": True
                        }
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "image",
                                "image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
                                "alt_text": "placeholder"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*배포 관리*"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": "Submitted by"
                            },
                            {
                                "type": "image",
                                "image_url": submitted_image_url,
                                "alt_text": "Dwight Schrute"
                            },
                            {
                                "type": "mrkdwn",
                                "text": submitted_name
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Production* 배포 \"해줘\""
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Front",
                                    "emoji": True
                                },
                                "value": "deploy-front",
                                "action_id": "deploy-front"
                            },
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Back",
                                    "emoji": True
                                },
                                "value": "deploy-back",
                                "action_id": "deploy-back"
                            }
                        ]
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "image",
                                "image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
                                "alt_text": "placeholder"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*로그 관리*"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": "Submitted by"
                            },
                            {
                                "type": "image",
                                "image_url": submitted_image_url,
                                "alt_text": "Dwight Schrute"
                            },
                            {
                                "type": "mrkdwn",
                                "text": submitted_name
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*로그* 내려 \"받아줘\""
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Back",
                                    "emoji": True
                                },
                                "value": "download-log-back",
                                "action_id": "download-log-back"
                            }
                        ]
                    }
                ]
            }
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 56300)))
