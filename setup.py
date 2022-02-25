from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

# with open("requirements.txt", "r") as rf:
#     requirements = rf.readlines()
#
# with open("requirements_dev.txt", "r") as rfd:
#     dev_requirements = rfd.readlines()

setup(
    name="pht-train-container-library",
    version="1.0.5",
    author="Michael Graf",
    author_email="michael.graf@uni-tuebingen.de",
    description="PHT train container library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/PersonalHealthTrain/implementations/germanmii/difuture/train-container-library.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["PHT", "security", "encryption", "personalhealthtrain", "docker"],
    python_requires=">=3.7",
    install_requires=[
        "aiohttp==3.8.0; python_version >= '3.6'",
        "aiosignal==1.2.0; python_version >= '3.6'",
        "async-timeout==4.0.0; python_version >= '3.6'",
        "attrs",
        "certifi==2021.10.8",
        "cffi==1.15.0",
        "charset-normalizer==2.0.7; python_version >= '3'",
        "click>=7.0.0; python_version >= '3.6'",
        "click-spinner==0.1.10",
        "colorama==0.4.4; sys_platform == 'win32' and platform_system == 'Windows' and platform_system == 'Windows'",
        "cryptography==35.0.0",
        "dnspython==2.1.0; python_version >= '3.6'",
        "docker==5.0.3",
        "email-validator==1.1.3",
        "fhir-kindling",
        "fhir.resources==6.1.0; python_version >= '3.6'",
        "fhirpy==1.2.1",
        "frozenlist==1.2.0; python_version >= '3.6'",
        "hvac==0.11.2",
        "idna==3.3; python_version >= '3'",
        "loguru==0.5.3",
        "multidict==5.2.0; python_version >= '3.6'",
        "numpy==1.21.3",
        "oauthlib==3.1.1",
        "orjson==3.6.4; python_version >= '3.7'",
        "pandas==1.3.4",
        "pendulum==2.1.2",
        "pika==1.2.0",
        "pycparser==2.20; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pydantic[email]==1.8.2; python_full_version >= '3.6.1'",
        "pypiwin32==223; sys_platform == 'win32'",
        "python-dateutil==2.8.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "python-dotenv==0.19.1",
        "pytz==2021.3",
        "pytzdata==2020.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pywin32==227; sys_platform == 'win32'",
        "pyyaml",
        "redis==3.5.3",
        "requests==2.26.0",
        "requests-oauthlib==1.3.0",
        "six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "tqdm==4.62.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "typing-extensions==3.10.0.2; python_version < '3.10'",
        "urllib3==1.26.7; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
        "websocket-client==1.2.1; python_version >= '3.6'",
        "win32-setctime==1.0.5; sys_platform == 'win32'",
        "xmltodict==0.12.0",
        "yarl==1.7.2; python_version >= '3.6'",
    ],
    extras_require={
        "dev": [
            "appdirs==1.4.4",
            "atomicwrites==1.4.0; sys_platform == 'win32'",
            "attrs==21.2.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "backports.entry-points-selectable==1.1.0; python_version >= '2.7'",
            "black==19.10b0; python_version >= '3.6'",
            "bleach==4.1.0; python_version >= '3.6'",
            "bump2version==1.0.5",
            "cached-property==1.5.2",
            "cerberus==1.3.4",
            "certifi==2021.10.8",
            "charset-normalizer==2.0.7; python_version >= '3'",
            "click==8.0.3; python_version >= '3.6'",
            "colorama==0.4.4; sys_platform == 'win32'",
            "coverage==6.0.2",
            "distlib==0.3.3",
            "docutils==0.18; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "filelock==3.4.0; python_version >= '3.6'",
            "ghp-import==2.0.2",
            "idna==3.3; python_version >= '3'",
            "importlib-metadata==4.8.1; python_version >= '3.6'",
            "iniconfig==1.1.1",
            "jinja2==3.0.2; python_version >= '3.6'",
            "keyring==23.2.1; python_version >= '3.6'",
            "markdown==3.3.4; python_version >= '3.6'",
            "markupsafe==2.0.1; python_version >= '3.6'",
            "mergedeep==1.3.4; python_version >= '3.6'",
            "mkdocs==1.2.3",
            "mkdocs-material==7.3.4",
            "mkdocs-material-extensions==1.0.5; python_version >= '3.6'",
            "orderedmultidict==1.0.5",
            "packaging==20.9; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pathspec==0.9.0",
            "pep517==0.12.0",
            "pip-shims==0.5.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "pipenv-setup==3.1.1",
            "pipfile==0.0.2",
            "pkginfo==1.7.1",
            "platformdirs==2.4.0; python_version >= '3.6'",
            "plette[validation]==0.2.3; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pluggy==1.0.5; python_version >= '3.6'",
            "py==1.10.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pygments==2.10.0; python_version >= '3.5'",
            "pymdown-extensions==9.0; python_version >= '3.6'",
            "pyparsing==3.0.2; python_version >= '3.6'",
            "pytest==6.2.5",
            "python-dateutil==2.8.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pywin32-ctypes==0.2.0; sys_platform == 'win32'",
            "pyyaml==6.0; python_version >= '3.6'",
            "pyyaml-env-tag==0.1; python_version >= '3.6'",
            "readme-renderer==30.0",
            "regex==2021.11.10",
            "requests==2.26.0",
            "requests-toolbelt==1.0.5",
            "requirementslib==1.6.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "rfc3986==1.5.0",
            "six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "toml==0.10.2; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "tomli==1.2.2; python_version >= '3.6'",
            "tomlkit==0.7.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "tox==3.24.5",
            "tqdm==4.62.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "twine==3.4.2",
            "typed-ast==1.4.3",
            "urllib3==1.26.7; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
            "virtualenv==20.9.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "vistir==0.5.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "watchdog==2.1.6; python_version >= '3.6'",
            "webencodings==0.5.1",
            "wheel==0.37.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "zipp==3.6.0; python_version >= '3.6'",
        ]
    },
)
