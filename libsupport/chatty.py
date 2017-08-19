#!python3

import random





def get_help():
    msg = """Help? Help? I can't help you, no one can...Here's your bloody help:
    - test1
        """
    return msg

def butt_joke(msg):
    db = []
    #db.append()
    db.append("Butts butts butts! All you talk about its BUTTS! I'm tired of this. brain the size of an asteroid, and all you can tell me are butt jokes")
    db.append("What has one mouth, no sense of humor, and talks about butts a lot? %s" % msg.author.name)
    db.append("I've heard that %s likes butts.. I can't lie, They don't much appeal to me" % msg.author.name)
    db.append("Have you heard the one about no cuts, no butts no coconuts? of course not... That's a few generations of evolution off for you lot.")
    db.append("Whats the difference between %s and a butt? I know a few grad students who are writing a thesis on it, but they haven't found an answer yet" % msg.author.name)
    return random.choice(db)
    
def face_joke(msg):
    db = []
    #db.append()
    db.append("Really %s, a 'your face' joke? Are you a bloody moron or something?" % msg.author.name)
    db.append(" oh '%s', You think you're clever or something?" % msg.content)
    db.append("'%s', Yes...that will teach them...Well done...Very brilliant... How high is your IQ? 7?(thats 1 more than 6...In case you were wondering)" % msg.content)
    db.append("I don't blame you for the face jokes. If i had a face like yours, I'd mock others faces too, %s" % msg.author.name)
    return random.choice(db)

def test_joke(msg):
    db = []
    #db.append()
    db.append("This is just a test, but its funnier than anything you'll come up with")
    return random.choice(db)
