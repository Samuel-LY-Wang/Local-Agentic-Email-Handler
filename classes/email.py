class email():
    def __init__(self, subject: str, sender: str, date: str, body: str, provider_args: dict = {}):
        self.subject = subject
        self.sender = sender
        self.date = date
        self.body = body
        self.provider_args = provider_args
    def __str__(self) -> str:
        return f"Subject: {self.subject}\nSender: {self.sender}\nDate: {self.date}\nBody: {self.body}"
    def create_new(self, **kwargs):
        """
        This method creates a new Email object with the same attributes as the current one, but allows for overriding any of them with new values.
        Other args (stored )
        """
        new_subject = kwargs.get('subject', self.subject)
        new_sender = kwargs.get('sender', self.sender)
        new_date = kwargs.get('date', self.date)
        new_body = kwargs.get('body', self.body)
        new_provider_args = self.provider_args.copy()
        for arg, val in kwargs.items():
            if arg not in ['subject', 'sender', 'date', 'body']:
                new_provider_args[arg] = val
        return email(new_subject, new_sender, new_date, new_body, new_provider_args)
    def to_json(self) -> dict:
        return {
            "subject": self.subject,
            "sender": self.sender,
            "date": self.date,
            "body": self.body
        }