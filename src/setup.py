from setuptools import setup
import setup_translate

pkg = 'Extensions.RemoteChannelStreamConverter'
setup(name='enigma2-plugin-extensions-remotechannelstreamconverter',
       version='3.0',
       description='Fetch channels from remote bouquets and make them available locally',
       package_dir={pkg: 'RemoteChannelStreamConverter'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
