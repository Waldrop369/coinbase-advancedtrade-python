from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='coinbase-advancedtrade-python',
    version='0.1.6',
    description='The unofficial Python client for the Coinbase Advanced Trade API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Rhett Reisman',
    author_email='rhett@rhett.blog',
    license='MIT',
    url='https://github.com/rhettre/coinbase-advancedtrade-python',
    packages=find_packages(),
    install_requires=requirements,
    keywords=['gdax', 'gdax-api', 'cbpro', 'cbpro-api', 'orderbook', 'trade', 'bitcoin', 'ethereum', 'BTC', 'ETH',
              'client', 'api', 'wrapper', 'exchange', 'crypto', 'currency', 'trading', 'trading-api', 'coinbase',
              'advanced-trade', 'prime', 'coinbaseadvancedtrade', 'coinbase-advanced-trade'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
