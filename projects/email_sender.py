import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()

    ##reciver mail
    receiver_mail= input("enter the receiver mail: ")
    ##mail  credential

    sender_email = "ashishkumar173217@gmail.com"
    password = "smpr wnbk cexw ibdw"

    server.login(sender_email,password)

    subject = input("Enter the subject : ")
    body = input("Enter te body : ")
    message = f"Subject : {subject} \n\n {body}"
    server.sendmail(sender_email,receiver_mail,message)
    print("mail sent successfuly")

    server.quit()

except Exception as e:
    print("An Error occured",e)