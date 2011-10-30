from setuptools import setup, find_packages

setup(name="django-paypal",
	version="0.1",
    description="Pluggable application that implements with PayPal Payments Standard and Payments Pro",
    author="John Boxall",
    author_email="john@mobify.me",
    packages=find_packages(),
    include_package_data=True,
)