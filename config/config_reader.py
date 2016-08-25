import configparser

cfg = configparser.ConfigParser()

cfg.read('settings.cfg')

print(cfg)

print(cfg['french'])
print(cfg['french']['greeting'])
print(cfg['files']['bin'])
