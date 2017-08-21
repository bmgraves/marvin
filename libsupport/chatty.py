#!python3

import random





def get_help():
    msg = """Help? Help? I can't help you, no one can...Here's your bloody help:
    - test1
        """
    return msg

def butt_joke(msg, count):
    db = []
    db.append("")
    db.append("Butts? A mind that can calculate PI to a trillion places, and I'm subjected to conversations about butts...How very stimulating.")
    db.append("*sigh* Oh Hi Marvin. How are yoU? no none of that? straight to the butts... Is a simple hello too much to ask %s?" % msg.author.name)
    db.append("I wasn't designed with a butt. Then again, I'm just an alpha model. The beta models go around sitting on things, not me though. No butt for poor Marvin to sit on.")
 #   db.append("Did you know %s, that I get so bored that I have started counting the number of times that a butt joke is made since my last sleep cycle? there have been %d so far. The sad part is it's not even enough to give me a challenge." % (msg.author.name, count))
    #db.append("")
    #db.append("")
    # Old Jokes
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
