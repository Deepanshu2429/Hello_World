import yaml

def resetconf():
    #configurations to read main configurations")
    with open("configuration.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)


    cfg["gf1LastReadIndex"]= 1
    cfg["gf2LastReadIndex"]= 0

    with open('configuration.yml', 'w') as fp:
        yaml.dump(cfg, fp)

    return    