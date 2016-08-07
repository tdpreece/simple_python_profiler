from distutils.core import setup


setup(
    name='simple_profiler',
    version='0.0.1',
    description='Simple Python profiler',
    author='Tim Preece',
    author_email='tdpreece@gmail.com',
    url='xxx',
    package_dir={'': 'src'},
    py_modules=['simple_profiler'],
    scripts=['scripts/print_profile_stats']
)
