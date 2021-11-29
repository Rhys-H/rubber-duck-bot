class RubberDuck:
    """
    Constructs the onboarding message and stores the state of which tasks were completed.
    """

    GREETING_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Quack! What are you working on? Quack! Quack! :duck:\n\n"
                "_Tell me your problems in the thread of this message, I won't judge!_"
            ),
        },
    }
    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel):
        self.channel = channel
        self.username = "RubberDuckBot"
        self.icon_emoji = ":duck:"
        self.timestamp = ""
        self.mark_as_solved = False
        self.asked_for_help = False

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.GREETING_BLOCK,
                self.DIVIDER_BLOCK,
                *self._get_reaction_block(),
                self.DIVIDER_BLOCK,
                *self._get_help_block(),
            ],
        }

    def _get_reaction_block(self):
        task_checkmark = self._get_checkmark(self.mark_as_solved)
        text = (
            f"{task_checkmark} *Have you solved your problem?\n"
            "Add a :white_tick: emoji if you solved your problem. "
            "This lets other ducks know you don't require any further assistance."
        )
        return self._get_task_block(text)

    def _get_help_block(self):
        task_checkmark = self._get_checkmark(self.asked_for_help)
        text = (
            # TODO Make this a button
            f"{task_checkmark} *Need backup from other ducks? Click this button to call for another duck!* :swan:\n"
            "This will tag another developer at random to listen to your problem. "
            "Don't be afraid to use this button more than once if it's a tricky problem."
        )
        return self._get_task_block(text)

    @staticmethod
    def _get_checkmark(task_completed: bool) -> str:
        if task_completed:
            return ":white_check_mark:"
        return ":white_large_square:"

    @staticmethod
    def _get_task_block(text):
        return [
            {"type": "section", "text": {"type": "mrkdwn", "text": text}},
        ]
