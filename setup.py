"""tfpipe setup script. """

from distutils.core import setup

setup(
    name='tfpipe',
    version='0.1.0',
    author='Karl Eklund',
    author_email='keklund@email.unc.edu',
    packages=['tfpipe', 
              'tfpipe.modules', 
              'tfpipe.modules.galaxy',
              'tfpipe.modules.gmap',
              'tfpipe.modules.cli',
              'tfpipe.modules.picard',
              'tfpipe.pipeline', 
              'tfpipe.utils',],
    scripts=['bin/example.py', 
             'bin/localhost.py',
             'bin/test.py'],
    url='http://fureylab.web.unc.edu',
    license='LICENSE.txt',
    description='Terry Furey Lab Pipeline',
    long_description=open('README.txt', 'r').read(),
)

#    install_requires=[],
