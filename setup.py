from distutils.core import setup


setup(
    name='profiler',
    version='0.0.1',
    description='Simple Python profiler',
    author='Tim Preece',
    author_email='tdpreece@gmail.com',
    url='xxx',
    package_dir={'': 'src'},
    py_modules=['profiler'],
    scripts=['scripts/print_stats']
)
