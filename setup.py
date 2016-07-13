from setuptools import setup


setup(
    name="flask-shell-ptpython",
    author="Jacopo Notarstefano",
    author_email="jacopo.notarstefano@gmail.com",
    description="Replace the default `flask shell` command with a similar command running Ptpython.",
    url="http://github.com/jacquerie/flask-shell-ptpython",
    version="0.0.1",
    py_modules=['flask_shell_ptpython'],
    install_requires=[
        'flask>=0.11',
        'click',
        'ptpython>=0.15',
    ],
    entry_points={
        'flask.commands': [
            'shell=flask_shell_ptpython:shell_command',
        ],
    },
)
