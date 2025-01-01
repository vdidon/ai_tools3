from distutils.core import setup
from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
    
setup(
    name="ai_tools",
    version="0.4.0",
    description="basic tools for ai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'opencv-python',
        'scipy',
        'Pillow',
        'imageio',
        'scikit-image',
        'DBUtils',
        'mysqlclient',  # Version Python 3 de MySQLdb
        'cognitive-face>=1.5.0',  # Pour l'API Microsoft Face
        'pandas',  # Pour le traitement des données
        'matplotlib',  # Pour pylab
        'scikit-learn',  # Pour sklearn
        'vcvf',  # Pour face_detector
        'vcvf_emotion',  # Pour face_emotion
        'zprint'
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={
        'ai_tools': ['data/clf.pkl','data/wjdc_clf_800.pkl'],
    },
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
    license = "MIT",
    author="vdidon",
    author_email="vdidon@live.fr",
    url="https://github.com/vdidon/ai_tools3",
    platforms = 'any'
)
