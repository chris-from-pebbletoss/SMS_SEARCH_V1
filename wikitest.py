from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import wikipedia


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    body = request.values.get('Body', None)
#     if (body):resp = MessagingResponse()
#     
    body = body.lower().rstrip().lstrip()
    subject = body

    try:
        info = wikipedia.summary(subject, sentences=2)
        resp.message("Hi! " + info)
    #if Disimbaguation error 
    except wikipedia.exceptions.DisambiguationError:
        newThings = wikipedia.search(subject)
        toReturn = "That's a bit broad. What specifically do you mean: "
        for element in newThings:
            toReturn = toReturn + " " + element + ","
        toReturn = toReturn + "."
        resp.message(toReturn)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
