import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()

__version = "0.0.0"

REPO_NAME = "chicken-desease-classification-Project"
AUTHOR_USER_NAME = "himanshu1104k"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "honey6k6@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
