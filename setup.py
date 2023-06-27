from setuptools import find_packages, setup

E_Var = '-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return package requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replaces("\n", "") for req in requirements]

        if E_Var in requirements:
            requirements.remove(E_Var)
            
    return requirements



setup(
    name= 'mlproject',
    version='0.0.1',
    author='Apuroop',
    author_email='apumutyala@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')




)