try:
    from config.config import __token__,__dev_token__, __admin__
except ImportError:
    print("Error has occured loading the config File")
