from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g.:
        # 'numpy',
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:main',  # Adjust this to the entry function of your app
        ],
    },
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dhanushyj/dsss_homework2',
    author='Your Name',
    author_email='your.email@example.com',
    description='A math quiz application',
    license='MIT',
)
