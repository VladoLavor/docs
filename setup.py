from setuptools import setup

setup(
    name='ProtoGen',
    version='1.0.0',
    packages=['plugins.protogen'],
    description='Generate API doc from proto files',
    install_requires=['gitpython', 'protobuf'],

    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'proto-gen = plugins.protogen.protogen:ProtoGen',
        ]
    },
)
