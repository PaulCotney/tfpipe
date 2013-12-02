"""tfpipe setup script. """

from distutils.core import setup

setup(
    name='tfpipe',
    version='0.1.4',
    author='Karl Eklund',
    author_email='keklund@email.unc.edu',
    packages=['tfpipe', 
              'tfpipe.utils',
              'tfpipe.modules', 
              'tfpipe.modules.cli',
              'tfpipe.modules.gmap',
              'tfpipe.modules.mach',
              'tfpipe.modules.plink',
              'tfpipe.modules.galaxy',
              'tfpipe.modules.picard',
              'tfpipe.modules.dfilter',
              'tfpipe.modules.bedtools',
              'tfpipe.modules.samtools',
              'tfpipe.modules.cufflinks',
              'tfpipe.pipeline',],
    scripts=['bin/tfpipe_run',
             'example/localhost.py',
             'example/kure.py'],
    url='http://fureylab.web.unc.edu',
    license='LICENSE.txt',
    description='Terry Furey Lab Pipeline',
    long_description=open('README.txt', 'r').read(),
)

#    install_requires=[],
