from setuptools import setup, find_packages

setup(
    name='blog-vini-django',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.2.1,<4.3',
        'psycopg2-binary>=2.9.6,<2.10',
        'Pillow>=9.5.0,<9.6',
        'django-summernote>=0.8.20.0',
        'python-dotenv>=1.1.0,<1.2',
        'django-axes>=8.0.0,<8.1',
    ],
)
