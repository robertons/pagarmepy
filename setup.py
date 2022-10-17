#!/usr/bin/env python

import setuptools

readme = open('README.md').read()

with open('requirements.txt') as reqs:
    requirements = reqs.read().split()

setuptools.setup(
    name='pagarmepy',
    version='0.0.1',
    description='SDK Python3 para Integração com Pagar.Me API V5',
    author='Roberto Neves',
    author_email='robertonsilva@gmail.com',
    url='https://github.com/robertons/pagarmepy',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet',
        'Topic :: Office/Business',
        'Topic :: Utilities'
    ],
    keywords='pagarme, pagar.me, pagar me, pagamento, cartão de crédito, boleto, pix, pagamentos, transações, payment, payments, credit-card'
)
