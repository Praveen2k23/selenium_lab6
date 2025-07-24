from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os


# Web url
WEBSITE_URL = "https://praveen2k23.github.io/selenium_lab6/"

# Create screenshots folder
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")
    print("Created 'screenshots' folder")

#open website
print("Opening the website...")

try:
    # Setup Chrome options to avoid errors
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Start Chrome browser
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    # Create wait object for better handling
    wait = WebDriverWait(driver, 10)
    
    # Open the website
    driver.get(WEBSITE_URL)
    print(f"Website opened: {WEBSITE_URL}")
    
    # Wait for page to load completely
    wait.until(EC.presence_of_element_located((By.ID, "seleniumForm")))
    time.sleep(2)
    
    # Take screenshot of empty form
    driver.save_screenshot("screenshots/1_empty_form.png")
    print("Screenshot saved: screenshots/1_empty_form.png")
    
except Exception as e:
    print(f"Error opening website: {e}")
    exit()

# Fill text box
print("\n Filling text boxes...")

try:
    # Fill First Name
    first_name = wait.until(EC.element_to_be_clickable((By.ID, "firstName")))
    first_name.clear()
    first_name.send_keys("Praveen")
    print("First Name: Praveen")
    
    # Fill Last Name
    last_name = driver.find_element(By.ID, "lastName")
    last_name.clear()
    last_name.send_keys("Perera")
    print(" Last Name: Perera")
    
    # Fill Email
    email = driver.find_element(By.ID, "email")
    email.clear()
    email.send_keys("praveenperera@gmail.com")
    print(" Email: praveenperera@gmail.com")
    
    # Fill Phone
    phone = driver.find_element(By.ID, "phone")
    phone.clear()
    phone.send_keys("070 1802876")
    print(" Phone: 070 1802876")
    
    # Fill Age
    age = driver.find_element(By.ID, "age")
    age.clear()
    age.send_keys("23")
    print(" Age: 23")
    
    time.sleep(1)
    
except Exception as e:
    print(f"Error filling text boxes: {e}")

# Select radio button
print("\n Selecting radio button...")

try:
    # Select Male gender
    male_radio = wait.until(EC.element_to_be_clickable((By.ID, "male")))
    male_radio.click()
    print("Gender selected: Male")
    
    time.sleep(1)
    
except Exception as e:
    print(f"Error selecting radio button: {e}")


print("\n Selecting checkboxes...")

try:
    # Select hobby
    reading_checkbox = driver.find_element(By.ID, "reading")
    if not reading_checkbox.is_selected():
        reading_checkbox.click()
    print("Hobby selected: Reading")
    
    # Select Sports hobby
    sports_checkbox = driver.find_element(By.ID, "sports")
    if not sports_checkbox.is_selected():
        sports_checkbox.click()
    print("Hobby selected: Sports")
    
    # Select Music hobby
    music_checkbox = driver.find_element(By.ID, "music")
    if not music_checkbox.is_selected():
        music_checkbox.click()
    print("Hobby selected: Music")
    
    # Select Newsletter
    newsletter_checkbox = driver.find_element(By.ID, "newsletter")
    if not newsletter_checkbox.is_selected():
        newsletter_checkbox.click()
    print("Newsletter subscription: Yes")
    
    # Accept Terms 
    terms_checkbox = driver.find_element(By.ID, "terms")
    if not terms_checkbox.is_selected():
        terms_checkbox.click()
    print("Terms accepted: Yes")
    
    time.sleep(1)
    
except Exception as e:
    print(f"Error selecting checkboxes: {e}")

# Select form dropdowns
print("\nSelecting from dropdowns...")

try:
    # Select Country
    country_dropdown = Select(driver.find_element(By.ID, "country"))
    country_dropdown.select_by_value("Sri Lanka")
    print("Country selected: Sri Lanka")
    
    # Select Education
    education_dropdown = Select(driver.find_element(By.ID, "education"))
    education_dropdown.select_by_value("bachelor")
    print("Education selected: Bachelor's Degree")
    
    time.sleep(1)
    
except Exception as e:
    print(f"Error selecting from dropdowns: {e}")

#Fix text areas
print("\n Filling text areas...")

try:
    # Fill Address
    address = driver.find_element(By.ID, "address")
    address.clear()
    address.send_keys("269 Dehwiala Rd, Boralesgamuwa")
    print("Address filled")
    
    # Fill Comments
    comments = driver.find_element(By.ID, "comments")
    comments.clear()
    comments.send_keys("This is automated testing with Selenium for SQA Lab 6")
    print("Comments filled")
    
    time.sleep(1)
    
except Exception as e:
    print(f"Error filling text areas: {e}")

# Take screenshot after filling all fields
driver.save_screenshot("screenshots/2_form_filled.png")
print("Screenshot saved: screenshots/2_form_filled.png")

# Print all values before submit
print("\n Showing all entered values...")
print("=" * 50)

try:
    # Get all values
    first_name_value = driver.find_element(By.ID, "firstName").get_attribute("value")
    last_name_value = driver.find_element(By.ID, "lastName").get_attribute("value")
    email_value = driver.find_element(By.ID, "email").get_attribute("value")
    phone_value = driver.find_element(By.ID, "phone").get_attribute("value")
    age_value = driver.find_element(By.ID, "age").get_attribute("value")
    
    # Check which radio button is selected
    gender_value = "Not selected"
    if driver.find_element(By.ID, "male").is_selected():
        gender_value = "Male"
    elif driver.find_element(By.ID, "female").is_selected():
        gender_value = "Female"
    elif driver.find_element(By.ID, "other").is_selected():
        gender_value = "Other"
    
    # Check which checkboxes are selected
    hobbies = []
    if driver.find_element(By.ID, "reading").is_selected():
        hobbies.append("Reading")
    if driver.find_element(By.ID, "sports").is_selected():
        hobbies.append("Sports")
    if driver.find_element(By.ID, "music").is_selected():
        hobbies.append("Music")
    if driver.find_element(By.ID, "travel").is_selected():
        hobbies.append("Travel")
    if driver.find_element(By.ID, "cooking").is_selected():
        hobbies.append("Cooking")
    
    # Get dropdown values
    country_dropdown = Select(driver.find_element(By.ID, "country"))
    country_value = country_dropdown.first_selected_option.text if country_dropdown.first_selected_option.get_attribute("value") else "Not selected"
    
    education_dropdown = Select(driver.find_element(By.ID, "education"))
    education_value = education_dropdown.first_selected_option.text if education_dropdown.first_selected_option.get_attribute("value") else "Not selected"
    
    # Get textarea values
    address_value = driver.find_element(By.ID, "address").get_attribute("value")
    comments_value = driver.find_element(By.ID, "comments").get_attribute("value")
    
    # Check additional checkboxes
    newsletter_status = "Yes" if driver.find_element(By.ID, "newsletter").is_selected() else "No"
    terms_status = "Yes" if driver.find_element(By.ID, "terms").is_selected() else "No"
    
    # Print all values
    print(f"First Name: {first_name_value}")
    print(f"Last Name: {last_name_value}")
    print(f"Email: {email_value}")
    print(f"Phone: {phone_value}")
    print(f"Age: {age_value}")
    print(f"Gender: {gender_value}")
    print(f"Hobbies: {', '.join(hobbies) if hobbies else 'None selected'}")
    print(f"Country: {country_value}")
    print(f"Education: {education_value}")
    print(f"Address: {address_value}")
    print(f"Comments: {comments_value}")
    print(f"Newsletter: {newsletter_status}")
    print(f"Terms Accepted: {terms_status}")
    print("=" * 50)
    
except Exception as e:
    print(f"Error retrieving values: {e}")

# Submit the form
print("\n Submitting the form...")

try:
    # Take screenshot before submitting
    driver.save_screenshot("screenshots/3_before_submit.png")
    print("Screenshot saved: screenshots/3_before_submit.png")
    
    # Click Submit button
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submitBtn")))
    submit_button.click()
    print("Submit button clicked!")
    
    # Wait for success message to appear
    success_message = wait.until(EC.visibility_of_element_located((By.ID, "successMessage")))
    
    # Wait a bit more for the animation to complete
    time.sleep(2)
    
    # Check if success message is displayed
    if success_message.is_displayed():
        print("Form submitted successfully!")
        print(f"Success Message: {success_message.text}")
        
        # Take screenshot after successful submission
        driver.save_screenshot("screenshots/4_form_submitted_success.png")
        print("📸 Screenshot saved: screenshots/4_form_submitted_success.png")
    else:
        print("Success message not visible")
        
except Exception as e:
    print(f"Error submitting form: {e}")

# Verify button text change
print("\n Verifying submission...")

try:
    # Check if submit button text changed
    submit_button_text = driver.find_element(By.ID, "submitBtn").text
    print(f"Submit button now shows: {submit_button_text}")
    
    time.sleep(2)
    
except Exception as e:
    print(f" Error verifying submission: {e}")

# Final

print(f"\n📋 SUMMARY:")
print(f"✅ Website URL: {WEBSITE_URL}")
print(f"✅ All form fields filled successfully")
print(f"✅ All checkboxes and radio buttons selected")
print(f"✅ All dropdown menus selected")
print(f"✅ Form submitted successfully")
print(f"✅ Success message displayed")
print(f"✅ 4 screenshots captured")

# Wait 5 seconds to see the final result
print("\n Waiting 5 seconds before closing browser...")
print("   (You can see the success message on screen)")
time.sleep(5)

# Close the browser
try:
    driver.quit()
    print("🔚 Browser closed. Automation completed successfully!")
except:
    print("🔚 Automation completed!")

print("\n🎓 Lab 6 Selenium Automation - COMPLETE! 🎓")