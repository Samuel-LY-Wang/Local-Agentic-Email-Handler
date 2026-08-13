"""
Put here the main things that must happen to run the email handler once.
Auto-running handled either through API or cronjob (added during installation) to run this script every 4 hours.
Process:
1. Authenticate w/ configured email provider
2. Read emails of the past 4 hours
3. Query configured LLM provider for response
4. Configuration-dependent, draft or send response emails
"""