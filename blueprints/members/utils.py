def is_email_unique(members: dict, email: str) -> bool:
    emails = list(map(lambda member: member['email'], members))
    return email in emails
