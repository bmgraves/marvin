try:
    from config.config import __token__,__dev_token__, __admin__,__channel__,__dev_channel__
except ImportError:
    print("Error has occured loading the config File")
