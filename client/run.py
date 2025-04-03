from configure import Configurator

config = Configurator()
conf_file = './conf.json'

if config.exists(conf_file):
    print('extracting data from configuration')
    data = config.extract_conf(conf_file)
else:
    print('creating a default configuration')
    config.create_conf(conf_file)

print('pre-load complete, starting application')

