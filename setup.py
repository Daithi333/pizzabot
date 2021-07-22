from setuptools import setup

setup(
    name='pizzabot',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'pizzabot=pizzabot.__main__:main'
        ]
    }
)
