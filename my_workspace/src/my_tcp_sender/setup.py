from setuptools import setup

package_name = 'my_tcp_sender'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='samar',
    maintainer_email='samarr@example.com',
    description='A ROS 2 package to send messages via TCP',
    license='License Type',
    entry_points={
        'console_scripts': [
            'tcp_sender_node = my_tcp_sender.tcp_sender_node:main',
        ],
    },
)

