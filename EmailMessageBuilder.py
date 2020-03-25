from EmailMessage import EmailMessage



class EmailMessageBuilder:

    def __init__(self):
        self._headerFields = {}
        self._emailMessage = EmailMessage()
        self._body = None
    
    def addHeaderField(self, headerField, headerFieldBody):
        if EmailMessage.validHeader(headerField) and EmailMessage.validHeaderFieldBody(headerFieldBody):
            self._headerFields[headerField] = headerFieldBody
        return self
    
    def setBody(self, body):
        self._body = body
        return self
    
    def create(self):
        for headerField, headerFieldBody in self._headerFields.items():
            self._emailMessage.appendMessage(f'{headerField}:{headerFieldBody}\r\n')
            self._emailMessage.appendMessage(f'\r\n')
            
        self._emailMessage.appendMessage(self._body)
        return self._emailMessage
            




def main():
    emailMessage = EmailMessageBuilder()\
    .addHeaderField(EmailMessage.TO, "edcarril@ucsd.edu")\
    .addHeaderField(EmailMessage.FROM, "edcarril@ucsd.edu")\
    .addHeaderField(EmailMessage.SUBJECT,"This is from myself to myself")\
    .setBody("Don't forget to turn off the AC when you leave your apartment.\n\nSincerely \n-Eddie")\
    .create()\
    .message()
    
    print(f'This is an example email message\n{emailMessage}')
    
    
if __name__ == "__main__" : main()