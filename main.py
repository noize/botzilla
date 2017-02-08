import socket, time
import threading
import sys
#from queue import Queue

""" bot_config class used to package information to give to bot so it can do its thing """
class bot_config:
    nick = ""

""" class for the actual bot """
class irc_bot:
    def __init__(self, server, port, channel, botconfig):
        self.server = server
        self.channel = channel
        self.port = port
        self.botconfig = botconfig

    def connect(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.server, self.port))

    def register(self):
        self.connection.send("USER {} {} {} : test bot lel\n\n".format(self.botconfig.nick, self.botconfig.nick, self.botconfig.nick))
        self.connection.send("NICK {}\n\n".format(self.botconfig.nick))
        self.connection.send("JOIN {}\n\n".format(self.channel))

    
    def evaluateMessages(self, **dict_to_check):
        
        d = dict_to_check
        
        loopRun = True
        
        while loopRun:
            try: 
                text = self.connection.recv(2040) 
                print text  
            except Exception: 
                pass

            for key in d:
                print key.lower()
                
                if text.lower().find(":{}".format(key.lower()))!=-1:
                    self.say(d[key])
            text=""
    
    def say(self, message):
        self.connection.send("PRIVMSG {} :{}\r\n".format(self.channel, message))
        
            
if (__name__ == "__main__"):
    conf = bot_config
    conf.nick = "BotzillaBot"
    bot = irc_bot("irc.freenode.net", 6667, "#BotzillaBotTesting", conf)
    bot.connect()
    bot.register()

    messagesToCheck = {"Hello" : "Hi im responding",
                       "Test" : "Responding to test"}
    
    bot.evaluateMessages(**messagesToCheck)
    while(True):pass #should be replaced later with more productive loop

