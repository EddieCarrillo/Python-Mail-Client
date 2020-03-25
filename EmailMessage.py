

#This is a just a wrapper around email message string
class EmailMessage:
   TRACE="trace"
   RESENT_DATE="resent-date"
   RESENT_FROM="resent-from"
   RESENT_SENDER="resent-sender"
   RESENT_TO="resent-to"
   RESENT_CC="resent-cc"
   RESENT_BCC="resent-bcc"
   RESENT_MSG_ID="resent-msg-id"
   ORIG_DATE="orig-date"
   FROM="from"
   SENDER="sender"
   REPLY_TO="reply-to"
   TO="to"
   CC="cc"
   BCC="bcc"
   MESSAGE_ID="message-id"
   IN_REPLY_TO="in-reply-to"
   REFERENCES="references"
   SUBJECT="subject"
   COMMENTS="comments"
   KEYWORD="keywords"
   OPTIONAL_FIELD="optional-field"

   _supported_header_fields = {TO,FROM,SUBJECT,CC,BCC,SENDER}   

   @staticmethod
   def validHeader(headerField):
      return isinstance(headerField, str) and headerField in EmailMessage._supported_header_fields
   #Implement when I get more time

   @staticmethod
   def validHeaderFieldBody(headerFieldBody):
      return True   

   def __init__(self):
      self._message = ""

   def appendMessage(self, str):
      self._message += str

   def message(self):
      return self._message


def main():
   print(EmailMessage.validHeader(EmailMessage.TO))
   
if __name__ == "__main__" : main()


