from setuptools import setup, find_packages

setup(name="TDDexample",
      version="0.1.0",
      description="Univariate linear regression of housing price against housing area",
      author="Dibya Chakravorty",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="dibyachakravorty@gmail.com",
      install_requires=["jupyter==1.0.0",
                        "matplotlib==3.3.4",
                        "numpy==1.19.5",
                        "pytest==6.2.4",
                        "pytest-mpl===0.13",
                        "pytest-mock==3.6.1",
                        "scipy==1.6.2",
                        ],
      )
