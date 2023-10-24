# "subprocess" module would be pretty much useful for executing system commands
import subprocess

# "re" module would be useful for matching regular expressions
import re

command = subprocess.run(["netsh", "wlan", "show", "profile"], capture_output=True).stdout.decode()
# Running a system command "netsh wlan show profile" and capturing the output
# and then decoding it to display only the required output
# without any return codes and errors

# print(command)
# We could make use of regular expressions
# All the profiles are listed after "All User Profile     :"
# profiles = re.findall("All User Profile     : (.*)", command)
# Output would be a list of user profiles with the escape sequence \r
# We'll filter the profiles without the escape sequence

print()
profiles = re.findall("All User Profile     : (.*)\r", command)
print('All the stored profiles : \n')
print(profiles)

# Let's make the program more interactive
print('\nEnter your choice : \n')

print('1. View the details of a particular profile')
print('2. View the details of all the profiles\n')

try:
    choice = int(input())
    # Read the user's choice
except (ValueError, KeyboardInterrupt):
    print('Interrupt received')
    print('Exiting the program')
    exit(1)

Wifi_list = list()

if (choice == 1):

    name = input("\nEnter the profile name you want to look at : ")

    if name in profiles:

        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()

        WiFi_profile = dict() # Dictionary to store SSID and Password of the profile

        WiFi_profile["SSID"] = name

        if (re.search("Security key           : Absent", profile_info)): # If there is no password
            WiFi_profile["Password"] = None

        elif (re.search("Security key           : Present", profile_info)): # if there is a password

            # Add the "key=clear" attribute to the above statement (profile_info)
            profile_password = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()

            security_key = re.search("Key Content            : (.*)\r", profile_password) # Search for the regular expression

            WiFi_profile["Password"] = security_key[1] # Output of the search gives two values, out of which the second value is the password

        print()
        print(WiFi_profile)

    else :
        print('\nWiFi Profile not found')

elif (choice == 2):

    print()

    for profile in profiles:

        WiFi_profile = dict() # Dictionary to store SSID and Password of the profile

        WiFi_profile["SSID"] = profile

        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", profile], capture_output=True).stdout.decode()

        if (re.search("Security key           : Absent", profile_info)): # If there is no password
            WiFi_profile["Password"] = None

        elif (re.search("Security key           : Present", profile_info)): # if there is a password

            # Add the "key=clear" attribute to the above statement (profile_info)
            profile_password = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True).stdout.decode()

            security_key = re.search("Key Content            : (.*)\r", profile_password) # Search for the regular expression

            WiFi_profile["Password"] = security_key[1] # Output of the search gives two values, out of which the second value is the password

        Wifi_list.append(WiFi_profile)

    for i in range(len(Wifi_list)):
        print(Wifi_list[i])
