import configparser

class Config:
    AMQPServer = ""
    AMQPPort = ""
    AMQPUser = ""
    AMQPPassword = ""
    AMQPVHost = ""

    def __init__(self, config_file="config.ini"):
        try:
            f = open(config_file, 'r')
            f.close()
            configure = configparser.ConfigParser()
            configure.read(config_file)
            self.AMQPServer = configure.get("Settings", "AMQPServer")
            self.AMQPPort = configure.get("Settings", "AMQPPort")
            self.AMQPUser = configure.get("Settings", "AMQPUser")
            self.AMQPPassword = configure.get("Settings", "AMQPPassword")
            self.AMQPVHost = configure.get("Settings", "AMQPVHost")
        except FileNotFoundError:
            config = configparser.ConfigParser()
            config.add_section("Settings")
            config.set("Settings", "AMQPServer", "")
            config.set("Settings", "AMQPPort", "")
            config.set("Settings", "AMQPUser", "")
            config.set("Settings", "AMQPPassword","")
            config.set("Settings", "AMQPVHost","")

            with open(config_file, "w") as cfile:
                config.write(cfile)
                print("Please check the "+str(config_file))
                exit()

config = Config()
