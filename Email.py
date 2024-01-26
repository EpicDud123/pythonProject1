# import smtplib, ssl
#
# port = 465  # For SSL
# password = "obrmzwmzleljqfaa"
# # Create a secure SSL context
# context = ssl.create_default_context()
#
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("epicep1c4314@gmail.com", password)
#     message = """\
# Subject: testing
#
# Fortnite."""
#     server.sendmail("epiccp1c4314@gmail.com", "generalbai3@gmail.com", message)
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

sender_email = "epicep1c4314@gmail.com"
receiver_email = "generalbai3@gmail.com"
password = "obrmzwmzleljqfaa"

message = MIMEMultipart("alternative")
message["Subject"] = "Great link just click ignore everything else"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
"""
html = """\
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Never Gonna Give You Up by Rick Astley</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #e6e6e6;
      }
        .container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  }
  
  h1 {
    color: #ff8c00;
    text-align: center;
  }
  
  p {
    font-size: 18px;
    line-height: 1.5;
  }
  
  img {
    display: block;
    margin: 0 auto;
    max-width: 100%;
    height: auto;
  }
  
  a {
    color: #ff8c00;
    text-decoration: none;
    font-weight: bold;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  .signature {
    text-align: right;
    font-style: italic;
  }
  
</style>
  </head>
  <body>
    <div class="container">
      <h1>Never Gonna Give You Up by Rick Astley</h1>
      <img src="https://i.imgur.com/5jwZaOj.jpg" alt="Rick Astley">
      <p>
        Dear friend,
      </p>
      <p>
        I hope this email finds you well. I wanted to share with you one of my all-time favorite songs, "Never Gonna Give You Up" by Rick Astley.
      </p>
      <p>
        This catchy tune was released in 1987 and has since become a classic. Its upbeat tempo, infectious chorus, and unforgettable music video have earned it a permanent place in pop culture history.
      </p>
      <p>
        If you haven't already, I highly recommend giving it a listen (or a re-listen!). You can find it on <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">YouTube</a> or on your favorite music streaming service.
      </p>
      <p>
        I hope you enjoy the song as much as I do!
      </p>
      <div class="signature">
        <p>Best regards,</p>
        <p>Your Name</p>
      </div>
    </div>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Load the image file
with open(r"C:\Users\WinstonBai\Downloads\goat.jpg", "rb") as f:
    image_data = f.read()

# Create the MIMEImage object
image_attachment = MIMEImage(image_data, name="amogus.jpg")

# Attach the image to the message
message.attach(image_attachment)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
