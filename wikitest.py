#THIS IS A COMMENT 
from flask import Flask, request, redirect
from flask import render_template
import wikipedia
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    body = request.values.get('Body', None)

    body = body.lower().rstrip().lstrip()

    # Add a message
    if "tell me about" in body:
        body = body[13:]
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


#@app.route('/')
#def runit():
#    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)














#import wikipedia



#account_sid = "AC881f1604ef165326e04770282e116a99"

#auth_token = "42f5091a441749bcff456fe9a2667451"

#client = Client(account_sid, auth_token)


#learn = input("What do you want to learn about:")
#myMessage = wikipedia.summary(learn, sentences=2)


#client.messages.create(
#	to="+12405853415",
#	from_="+12673100434", 
#	body = myMessage
#	)
#print("Done")

