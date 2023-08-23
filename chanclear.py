#made by gh0st
#visit IRC.TWISTEDNET.ORG CHANNEL #TWSITED & #DEV 

#To clear all exemptions in the channel the bot is in, first ensure the bot has 'op' permissions. Then, simply send the bot a message with the word 'clear'.


import ssl
import irc.bot
import irc.connection
import time
from jaraco.stream import buffer

class GhostBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=9999):
        irc.client.ServerConnection.buffer_class = buffer.LenientDecodingLineBuffer

        factory = irc.connection.Factory(wrapper=ssl.wrap_socket)
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname, connect_factory=factory)
        self.channel = channel
        self.is_processing_exempts = False
        self.exempts = []
        self.invites = []

    def on_all_raw_messages(self, c, e):
        if e.arguments[0].startswith(":irc.servercentral.net 348"):
            self.exempts.append(e.arguments[0].split()[4])

        elif e.arguments[0].startswith(":irc.servercentral.net 346"):
            self.invites.append(e.arguments[0].split()[4])

        if self.is_processing_exempts and "End of Channel Exception List" in e.arguments[0]:
            for exempt in self.exempts:
                c.mode(self.channel, "-e {}".format(exempt))
            self.exempts = []

        if self.is_processing_exempts and "End of Channel Invite List" in e.arguments[0]:
            for invite in self.invites:
                c.mode(self.channel, "-I {}".format(invite))
            self.invites = []

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        sender = e.source.nick
        message = e.arguments[0]

        if message.lower() == "clear":
            self.remove_exempts(c)
            c.privmsg(sender, "Exempts and invite exemptions cleared.")

    def on_pubmsg(self, c, e):
        pass

    def on_disconnect(self, c, e):
        time.sleep(5)
        self.jump_server()

    def remove_exempts(self, c):
        self.is_processing_exempts = True
        self.exempts = []
        self.invites = []
        c.send_raw("MODE {} +e".format(self.channel))
        c.send_raw("MODE {} +I".format(self.channel))

def main():
    server = "irc.servercentral.net"
    port = 9999
    channel = "#gg"
    nickname = "GhostBot"

    bot = GhostBot(channel, nickname, server, port)
    bot.start()

if __name__ == "__main__":
    main()
