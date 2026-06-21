from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    user_message = ""
    bot_reply = ""


    if request.method == "POST":

        user_message = request.form["message"].lower()

        if user_message == "hello":
            bot_reply = "Hi! How can I help you?"

        elif user_message == "how are you":
            bot_reply = "I am fine."

        elif user_message == "bye":
            bot_reply = "Goodbye!"

        elif user_message == "services":
            bot_reply = "We provide Cloud Computing, Web Development and AI services."
        
        elif user_message == "internship":
            bot_reply = "CodeAlpha provides internships in various domains."

        elif user_message == "cloud computing":
            bot_reply = "Cloud computing delivers computing services over the internet."

        elif user_message == "thank you":
            bot_reply = "You're welcome!"

        elif user_message == "help":
            bot_reply = "You can ask about services, contact, about, or internship."
            
        elif user_message == "contact":
            bot_reply = "Email: services@codealpha.tech"

        elif user_message == "about":
            bot_reply = "This is a chatbot developed for the CodeAlpha Internship."    
        
        elif user_message == "help":
            bot_reply = "You can ask about services, contact, or about."

        elif user_message == "thank you":
            bot_reply = "You're welcome!"

        elif user_message == "who are you":
            bot_reply = "I am CodeAlpha Chatbot."
        else:
            bot_reply = "Sorry, I don't understand."

    return render_template("index.html", user_message=user_message,reply=bot_reply)

if __name__ == "__main__":
    app.run(debug=True)