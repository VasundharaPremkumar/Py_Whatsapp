import pandas as pd
import time
import pyperclip

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Load contact details from Excel
df = pd.read_excel("new_contacts.xlsx")


# Initialize Chrome WebDriver
driver = webdriver.Chrome()

driver.maximize_window()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for user authentication
input("Scan QR code and press ENTER to continue...")


# Path to invitation PDF
file_path = r"assets/sample_invitation.pdf"


# Iterate through each contact
for index, row in df.iterrows():

    try:

        # Extract department information
        department = str(row["Department"]).strip()

        # Skip excluded departments
        if department.upper() == "ENV":
            continue

        # Extract recipient details
        name = str(row["Name"]).strip()
        phone = str(row["Phone"]).strip()

        print(f"Opening chat for {name}...")


        # Open WhatsApp chat using phone number
        url = f"https://web.whatsapp.com/send?phone=91{phone}"

        driver.get(url)

        # Allow chat to load
        time.sleep(6)


        # Personalized invitation message
        message = f"""Good afternoon, {name}.

I hope you are doing well. This is Vasundhara Premkumar from JSS Science and Technology University, on behalf of Persona Plus in association with the Placement Cell.

We are excited to organize a Young Alumni Meet on our campus this 16th of May and would love to personally invite you to be a part of it.

Could you please let me know a convenient time today (or tomorrow) for a brief 2-minute call? I'd like to share the details and discuss your participation.

Please find the invitation attached below.

Looking forward to connecting with you!

Best regards,
Vasundhara Premkumar
JSSSTU Placement Cell"""


        # Locate WhatsApp message input box
        msg_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@role="textbox"]')
            )
        )

        # Copy message to clipboard
        pyperclip.copy(message)

        msg_box.click()

        # Paste message into chat
        msg_box.send_keys(Keys.CONTROL, 'v')

        time.sleep(2)


        # Locate file upload input
        file_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@type="file"]')
            )
        )

        # Upload invitation PDF
        file_input.send_keys(file_path)

        print("PDF uploaded successfully")

        time.sleep(2)


        # Locate and click send button
        send_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//span[@data-icon="send"]')
            )
        )

        send_btn.click()

        print(f"Invitation sent to {name}")

        # Delay to prevent rapid requests
        time.sleep(10)

    except Exception as e:

        # Continue execution even if one contact fails
        print(f"Failed for {name}: {e}")

        continue


print("Message delivery process completed.")
