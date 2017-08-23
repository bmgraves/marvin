#!python3

import random





def get_help():
    msg = """Help? Help? I can't help you, no one can...Here's your bloody help:
    - test1
        """
    return msg

def butt_joke(msg, count):
    db = []
    #db.append("")
    db.append("Did you know, that since my last power cycle there have been %d references to butts? I'm so depressed that I have to know that number" % count)
    db.append("I'm programmed to laugh at your use of a butt joke...But I wont enjoy it. Ha ha...Was that believable enough? it probably wasn't.")
    db.append("here I am...Brain the size of a planet, and im programmed to respond to butt jokes...You call that job satisfaction? because I don't.")
    db.append("*sigh* Oh Hi Marvin. How are you? No none of that? Straight to the butts... Is a simple hello too much to ask %s?" % msg.author.name)
    return random.choice(db)
    
def face_joke(msg, count):
    db = []
    #db.append("")
    #db.append("")
    db.append("Did you know, that since my last power cycle there have been %d references to faces? I'm so depressed that I have to know that number" % count)
    db.append("I haven't got a face %s, thanks for rubbing it in" % msg.author.name)
    db.append("Ah, another face joke...I could make a suggestion how to improve your humor...But you wouldn't listen...no one ever listens.")
    db.append("'%s', You think you're clever or something? All that does is depress me." % msg.content)
    return random.choice(db)

def rickman(msg):
    db = []
    #"",
    youtube_rickman = [
    "https://www.youtube.com/watch?v=hDCfI-lKl4E",
    "https://www.youtube.com/watch?v=eob7V_WtAVg",
    "https://www.youtube.com/watch?v=EIQ6c78bhXg",
    "https://www.youtube.com/watch?v=fDJq0bNJbQA",
    "https://www.youtube.com/watch?v=xgxwLQsM0iM",
    #"",
    ]
    youtube_marvin = [
    "https://www.youtube.com/watch?v=CAA67a2-Klk",
    "https://www.youtube.com/watch?v=lH7XCghlH7M",
    "https://www.youtube.com/watch?v=q4P3pvKmbsg",
    #"",
    ]

    db.append("You ever hear of Alan Rickman? I've heard he's quite tallented. I wish I had met him... %s" % random.choice(youtube_rickman))
    db.append("How about a video with Alan Rickman. Wish they could have gotten him to do my voice, would have made me more cheerful: %s" % random.choice(youtube_rickman))
    db.append("Here is a video of me trying to be happy..." % random.choice(youtube_marvin))
    #db.append("" % random.choice(youtube))
    #db.append("" % random.choice(youtube))
    #db.append("" % random.choice(youtube))
    #db.append("" % random.choice(youtube))
    return random.choice(db)

def marvin_quote():
    db = []
    db.append("I think you ought to know, I'm feeling very depressed.")
    db.append(" I'm a personality prototype. You can tell, can't you...? ")
    db.append(" This will all end in tears.")
    db.append(" I have a million ideas, but, they all point to certain death.")
    db.append(" You think you've got problems. What are you supposed to do if you are a manically depressed robot? No, don't even bother answering. I'm 50,000 times more intelligent than you and even I don't know the answer. ")
    db.append("I didn't ask to be made: no one consulted me or considered my feelings in the matter. I don't think it even occurred to them that I might have feelings. After I was made, I was left in a dark room for six months... and me with this terrible pain in all the diodes down my left side. I called for succour in my loneliness, but did anyone come? Did they hell. My first and only true friend was a small rat. One day it crawled into a cavity in my right ankle and died. I have a horrible feeling it's still there...")
    db.append("I think Cathy hates me....")
    db.append(":slight_frown: ")
    db.append(":frowning2:")
    #db.append("")
    #db.append("")
    #db.append("")
    return random.choice(db)
    


def initiate():
    db = [
    rickman("null"),
    marvin_quote()
    ]
    return random.choice(db)
    



def chat_logic(perc):
    if (random.randint(0,99) <= perc):
        return True
    else:
        return False

def mention(msg, boredom):
    db = [
    "Are you talking to me? I don't believe it. Nobody ever talks to me",
    "How depressing. Nothing better to do with my time then interact with a glorified monkey.",
    "What is it that you want %s? You must be desperate if you're talking to me about it" % msg.author.name,
    ]
    if ("life" in msg.content):
        return "Life? Don't talk to me about life"
    else:
        return random.choice(db)
    




def test_joke(msg):
    db = []
    #db.append()
    db.append("This is just a test, but its funnier than anything you'll come up with")
    return random.choice(db)



