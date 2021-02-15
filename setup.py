import setuptools

setuptools.setup(
    name='cryptopycode',
    version='0.0.2',
    author="Alex",
    author_email='seriousalsir@gmail.com',
    description='Encryption and decryption on the key of the python module',
    url="https://github.com/alserious/cryptopycode",
    packages=setuptools.find_packages(),
    install_requires=[
        'cryptography'
    ],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
