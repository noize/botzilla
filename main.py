import socket

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
        self.register()
        while(True): # for debug purpouses
            print self.connection.recv(1024)

    def register(self):
        self.connection.send("USER {} {} {} : test bot lel\n\n".format(self.botconfig.nick, self.botconfig.nick, self.botconfig.nick))
        self.connection.send("NICK {}\n\n".format(self.botconfig.nick))
        self.connection.send("JOIN {}\n\n".format(self.channel))

if (__name__ == "__main__"):
    conf = bot_config
    conf.nick = "testBotzillaBot"
    bot = irc_bot("irc.freenode.net", 6667, "#tempBotzillaChat", conf)
    bot.connect()
    bot.register()
