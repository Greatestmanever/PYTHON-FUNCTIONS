# Combine the first name and last name into a single "Full Name"

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name(" greatman", "JUSTUS"))

