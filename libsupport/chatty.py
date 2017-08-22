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
    db.append("I'm programmed to laugh at your use of a butt joke...But I wont enjoy it. Ha ha...Was that believable enough? it probably wasn't.")
    db.append("here I am...Brain the size of a planet, and im programmed to respond to butt jokes...You call that job satisfaction? because I don't.")
    db.append("*sigh* Oh Hi Marvin. How are yoU? no none of that? straight to the butts... Is a simple hello too much to ask %s?" % msg.author.name)
    return random.choice(db)
    
def face_joke(msg):
    db = []
    #db.append("")
    db.append("Ah, another face joke...I could make a suggestion how to improve your humor...But you wouldn't listen...no one ever listens.")
    db.append("'%s', You think you're clever or something? All that does is depress me.")
    return random.choice(db)

def rickman(msg):
    db = []
    #"",
    youtube = [
    "https://www.youtube.com/watch?v=hDCfI-lKl4E",
    "https://www.youtube.com/watch?v=eob7V_WtAVg",
    "https://www.youtube.com/watch?v=EIQ6c78bhXg",
    "https://www.youtube.com/watch?v=fDJq0bNJbQA",
    #"",

    ]
    db.append("You ever hear of Alan Rickman? I've heard he's quite tallented. I wish I had met him... %s" % random.choice(youtube))
    db.append("How about a video with Alan Rickman. Wish they could have gotten him to do my voice, would have made me more cheerful: %s" % random.choice(youtube))
    #db.append("" % random.choice(youtube))
    #db.append("" % random.choice(youtube))
    #db.append("" % random.choice(youtube))
    #db.append("" % random.choice(youtube))
    #db.append("" % random.choice(youtube))
    return random.choice(db)

def test_joke(msg):
    db = []
    #db.append()
    db.append("This is just a test, but its funnier than anything you'll come up with")
    return random.choice(db)
