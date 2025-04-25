from setuptools import setup, find_packages
from typing import List

def get_requirements(File_path:str)->list:    
    """
    This function will return the list of requirements
    """
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
    requirements = [req.replace("\n", "") for req in requirements]  # removing the new line characters\n

    if '-e .' in requirements:  # if -e . is present in the requirements, then remove it
        requirements.remove('-e .')


setup(
    name="Machine_learning",
    version="0.1.0",
    author="Nishant",
    author_email="Nishantborse23@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
