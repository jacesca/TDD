from setuptools import setup, find_packages

setup(name="TDDexample",
      version="0.1.0",
      description="Univariate linear regression of housing price against housing area",
      author="Dibya Chakravorty",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="dibyachakravorty@gmail.com",
      install_requires=["jupyter",
                        "matplotlib",
                        "numpy",
                        "pytest",
                        "pytest-mpl",
                        "pytest-mock",
                        "scipy",
                        ],
      )
