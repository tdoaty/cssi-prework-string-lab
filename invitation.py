
### Challenge 1 - Percy Replacement:
def percy_replacer(string_about_percy):
  return string_about_percy.replace("Percy", "Ron")

### Challenge 2 - String Interpolation:
def weasley_invitation(name,day,date,month):
  return "The family of {first_name} Weasley proudly invite you to celebrate their graduation from Hogwarts on {day} the {date} of {month}. Festivities will be held at The Burrow. See you then!".format(first_name = name, day = day, date = date, month = month)
  print weasley_invitation.format("Ron", "Sunday", "May", "18th")

### Challenge 3 - Seating Location
def seating_location(last_name):
    if last_name[0] == 'W'
        location = "front row."
    else:
    if last_name[0] == "A"
        location = "rear section."
    else:
    if last_name[0] == "B"
        location = "rear section."
    else:
    if last_name[0] == "C"
        location = "rear section."
    else:
    if last_name[0] == "D"
        location = "rear section."
    else:
    if last_name[0] == "E"
            location = "rear section."
    else:
    if last_name[0] == "F"
            location = "rear section."
    else:
    if last_name[0] == "G"
            location = "rear section."
    else:
    if  last_name[0] =="W"
        location = "front row."
    else:
        location = "middle section."
  return "You have a reserved seat in the {section}".format(section = location)

###Challenge 4 - All Together
def create_invitation(first_name, last_name, message):
  return first_name.upper() + "./n" + message + "\nP.S. "+ seating_location(last_name)
