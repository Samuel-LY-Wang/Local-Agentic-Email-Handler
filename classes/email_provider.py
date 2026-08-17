from typing import List
from classes.email import email

class base_email_provider:
    """
    This is a Java-style interface storing information about an email provider and some functions for authenticating, reading emails, anddrafting/sending a new email.
    It will not work unless overridden by subclasses.
    """
    def __init__(self, name: str):
        self.name = name
    def authenticate(self) -> bool:
        """
        This is meant to be a Java-style interface for authenticating with a provider. It should be overridden by subclasses.
        """
        raise NotImplementedError("This method must be overridden by subclasses.")
    def remove_acc(self):
        """
        This is meant to be a Java-style interface for removing an account from a provider. It should be overridden by subclasses.
        """
        raise NotImplementedError("This method must be overridden by subclasses.")
    def check(self) -> List[email]:
        """
        This method is a Java-style interface for reading emails from a provider. It must be overridden by subclasses.
        """
        raise NotImplementedError("This method must be overridden by subclasses.")
    def draft(self, new_email: email):
        """
        This method is a Java-style interface for adding an email to the draft folder of a provider.
        If the provider supports a draft folder, this function must be overridden by subclass.
        The parameters provided here may not be changed, as this is an interface.
        """
        raise NotImplementedError("This method must be overridden by subclasses.")
    def send(self, new_email: email):
        """
        This method is a Java-style interface for sending an email from a provider.
        The parameters provided here may not be changed, as this is an interface.
        """
        raise NotImplementedError("This method must be overridden by subclasses.")