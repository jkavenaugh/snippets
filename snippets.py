"""

Python 3 Snippets!

"""

# Email Log through RackSpace

import smtplib
from email.mime.text import MIMEText

mail_to = 'destination@null.com'
mail_username = 'my@email.com'
mail_password = 'supersecretpassword'

def send_report(log_content):

    """ Send some reporting
    """

    text_subtype = 'plain'
    content = mail_from+' Log Processed: '+today.strftime('%a, %d %b %Y %H:%M:%S')+'\r'
    if log_content:
        content += 'Logging follows: \r'
        content += str(log_content)


    msg = MIMEText(content, text_subtype)
    if 'ERROR' in str(log_content):
        msg['Subject'] = mail_from+': Error processing'
    else:
        msg['Subject'] = mail_from+': Success processing'
        msg['Subject'] = mail_from
    msg['From'] = mail_from
    msg['To'] = mail_to

    server = smtplib.SMTP_SSL('secure.emailsrvr.com')
    server.login(mail_username, mail_password)
    server.sendmail(mail_username, mail_to, msg.as_string())
    server.quit()

# Logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
log_string = io.StringIO()
ch = logging.StreamHandler(log_string)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info('This is some info')
logger.error('This is an error')

log_content = log_string.getvalue()
log_string.close()
ch.flush()

# Mysql

mydb = mysql.connector.connect(user = mysql_user, password = mysql_pass, host = mysql_host, database = mysql_db)

# Get rows

my_cursor = mydb.cursor()
  
my_cursor.execute("""
                  SELECT *
                  FROM table
                  """)

    for (blah) in my_cursor:
         pring(blah)


# Insert

my_cursor.execute("""
                  INSERT INTO table
                  (value1, value2)
                  VALUES
                  (%s, %s)
                  """, 
                  (value1, value2))

    my_cursor.close()

# sniff raw socket

import socket

eth = 'enp2s0'

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 3)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((eth, 3))

data = s.recvfrom(65565)