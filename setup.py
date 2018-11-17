import os

from setuptools import find_packages, setup

PACKAGE_DIR = os.path.join(os.path.dirname(__file__), 'konst')


def _read_version():
    with open(os.path.join(PACKAGE_DIR, '__init__.py'), 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[-1].strip().strip('\'"')


def main():
    setup(
        name='konst',
        version=_read_version(),
        packages=find_packages(exclude=['tests']),
        python_requires=">=3.6",
        classifiers=(
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ),
    )


if __name__ == '__main__':
    main()
