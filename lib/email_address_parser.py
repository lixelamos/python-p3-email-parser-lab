class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        addresses = self.email_addresses.replace(",", " ").split()
        unique_addresses = list(set(addresses))
        sorted_addresses = sorted(unique_addresses)
        email_addresses = [address for address in sorted_addresses if self.is_email(address)]
        return email_addresses

    def is_email(self, string):
        # Use a simple regex pattern to check if the string is a valid email address
        import re
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        return re.match(pattern, string) is not None
