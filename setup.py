#It turns codebase into an installable Python package.
#This improves modularity, makes code importable across files, and simplifies sharing or deploying the project

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
        This function will return list of requirements
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()     #to remove empty spaces
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst

# testing - print(get_requirements())

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author= "Aryan Khurana",
    author_email= "aryankhurana1701@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()

)
# put -e . in requirements.txt file to convert this project into a package