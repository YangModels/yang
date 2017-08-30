from setuptools import setup

setup(
    name='yang',
    version='',
    packages=['tools', 'tools.api', 'tools.recovery', 'tools.validate', 'tools.runYANGallstats',
              'tools.parseAndPopulate', 'tools.ietfYangDraftPull', 'tools.utility'],
    url='',
    license='',
    author='Miroslav Kovac',
    author_email='',
    description='', install_requires=['jinja2', 'numpy', 'pyang', 'requests', 'travispy', 'flask', 'Crypto', 'pika']
)
