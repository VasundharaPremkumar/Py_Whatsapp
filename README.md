# WhatsApp Alumni Invitation Automation

An automation project built to streamline bulk WhatsApp outreach for a college alumni event using Python and Selenium.

This project was created during the organization of a **Young Alumni Meet** at JSS Science and Technology University. Instead of manually saving hundreds of phone numbers and sending invitations individually, this automation script sends personalized WhatsApp messages along with a PDF invitation attachment directly through WhatsApp Web.

The entire outreach process that would normally take several hours was reduced to under an hour using automation.

---

## Project Overview

Managing alumni communication manually can be repetitive and time-consuming. This project automates the workflow by:

- Reading contact details from an Excel sheet
- Opening WhatsApp chats automatically
- Sending personalized invitation messages
- Attaching invitation PDFs
- Skipping selected departments dynamically
- Handling errors gracefully during execution

---

## Features

- Bulk WhatsApp message automation
- Personalized messages using recipient names
- PDF invitation attachment support
- Excel-based contact management
- Automated browser interaction using Selenium
- Department filtering logic
- Exception handling for failed deliveries
- Time-efficient outreach workflow

---

## Tech Stack

- Python
- Selenium WebDriver
- Pandas
- Pyperclip
- WhatsApp Web

---

## How the Code Works

### 1. Load Contact Data
The script reads alumni contact information from an Excel file using Pandas.

```python
df = pd.read_excel("new_contacts.xlsx")
```

The Excel sheet contains:
- Name
- Phone Number
- Department

---

### 2. Launch WhatsApp Web
Chrome is opened using Selenium WebDriver and the user logs in by scanning the QR code.

```python
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
```

---

### 3. Filter Contacts
The script skips recipients belonging to specific departments (e.g., ENV).

```python
if department.upper() == "ENV":
    continue
```

---

### 4. Generate Personalized Message
Each recipient receives a customized invitation message using their name dynamically.

```python
message = f"Good afternoon, {name}..."
```

---

### 5. Open WhatsApp Chat
The script automatically opens the recipient’s WhatsApp chat using their phone number.

```python
url = f"https://web.whatsapp.com/send?phone=91{phone}"
```

---

### 6. Attach Invitation PDF
The invitation PDF is uploaded automatically through WhatsApp Web.

```python
file_input.send_keys(file_path)
```

---

### 7. Send Message
The script clicks the send button and delivers the invitation.

```python
send_btn.click()
```

---

### 8. Error Handling
If any contact fails, the script logs the error and continues execution without stopping the entire process.

```python
except Exception as e:
```

---

## Folder Structure

```bash
├── slecect.py
├── new_contacts.xlsx
├── invite.pdf
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python slecect.py
```

---

## Requirements

Create a `requirements.txt` file with:

```txt
pandas
selenium
pyperclip
openpyxl
```

---

## Real-World Impact

This project demonstrates how automation can solve practical communication problems efficiently.

### Result:
- Reduced manual outreach effort drastically
- Automated alumni invitation workflow
- Saved several hours of repetitive work
- Improved event coordination efficiency

---

## Future Improvements

- CSV and Google Sheets integration
- GUI dashboard
- Scheduled messaging
- Image and video attachment support
- Contact validation
- Logging and analytics
- Multi-language message templates

---

## Important Note

This project is intended strictly for educational, organizational, and productivity purposes.

Please use automation responsibly and ensure compliance with WhatsApp policies and recipient consent guidelines.

---

## Author

**Vasundhara Premkumar**

Built to simplify alumni outreach through practical automation.
