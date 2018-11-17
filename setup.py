import os

from setuptools import find_packages, setup

PACKAGE_DIR = os.path.join(os.path.dirname(__file__), 'konst')


def _read_version():
    with open(os.path.join(PACKAGE_DIR, '__init__.py'), 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[-1].strip().strip('\'"')
        raise ValueError('Could not find __version__')


def main():
    setup(
        name='konst',
        version=_read_version(),
        description='Effortless, meaningless, DRY constants',
        packages=find_packages(exclude=['tests']),
        python_requires=">=3.6",
        extras_require={'dev': ['isort', 'black', 'pytest', 'pytest-watch']},
        classifiers=(
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ),
    )


if __name__ == '__main__':
    main()
