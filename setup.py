from setuptools import setup, find_packages
import os
import glob
from setuptools.command.build_py import build_py
import shutil


class CustomBuildPy(build_py):
    """Custom build command to copy API directories into gpapis package"""
    
    def run(self):
        # Run the standard build
        build_py.run(self)
        
        # Copy API directories into the built gpapis package
        api_dirs = ['BROKER', 'CONTACTLESS', 'CORE', 'OPEN', 'SCPP', 'UPGRADE']
        
        for api_dir in api_dirs:
            if os.path.exists(api_dir):
                # Source directory in the original location
                src_dir = api_dir
                # Destination directory in the built package
                dst_dir = os.path.join(self.build_lib, 'gpapis', api_dir.lower())
                
                # Create destination directory if it doesn't exist
                os.makedirs(dst_dir, exist_ok=True)
                
                # Copy the entire directory tree
                if os.path.exists(dst_dir):
                    shutil.rmtree(dst_dir)
                
                shutil.copytree(src_dir, dst_dir)
                print(f"Copied {src_dir} to {dst_dir}")
        
        # Copy the license file to the built package
        license_file = 'GP-Specification-License-Agreement.pdf'
        if os.path.exists(license_file):
            dest_license_path = os.path.join(self.build_lib, 'gpapis', 'GP-Specification-License-Agreement.pdf')
            shutil.copy2(license_file, dest_license_path)
            print(f"Copied {license_file} to {dest_license_path}")


# Function to get all package data (the API specification files)
def get_package_data():
    package_data = []
    
    # Define the API directories to include
    api_dirs = ['BROKER', 'CONTACTLESS', 'CORE', 'OPEN', 'SCPP', 'UPGRADE']
    
    for api_dir in api_dirs:
        if os.path.exists(api_dir):
            # Include all files in each API version subdirectory
            for root, dirs, files in os.walk(api_dir):
                for file in files:
                    # Get the relative path from the API directory
                    rel_path = os.path.relpath(os.path.join(root, file), api_dir)
                    # Map to the gpapis subdirectory structure
                    package_data.append(f"gpapis/{api_dir.lower()}/{rel_path}")
    
    # Include the license file
    if os.path.exists('GP-Specification-License-Agreement.pdf'):
        package_data.append('GP-Specification-License-Agreement.pdf')
    
    return package_data

# Read version from __init__.py to ensure consistency
import re
def get_version():
    """Extract version from the gpapis __init__.py file"""
    with open('gpapis/__init__.py', 'r', encoding='utf-8') as f:
        content = f.read()
        # Find the version line
        version_match = re.search(r"__version__\s+=\s+[\'\"]([^\'\"]*)[\'\"]", content)
        if version_match:
            return version_match.group(1)
        else:
            raise RuntimeError("Unable to find version string.")

setup(
    name="gpapis",
    version=get_version(),
    author="ibaibing",
    author_email="ibaibing@outlook.com",
    description="GlobalPlatform API specifications and binaries for SmartCard/Secure Element development",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/ibaibing/globalplatform-apis",
    packages=find_packages(include=['gpapis', 'gpapis.*']),
    package_data={
        'gpapis': get_package_data(),
    },
    include_package_data=True,
    cmdclass={
        'build_py': CustomBuildPy,
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GlobalPlatform Specification License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Java Libraries",
    ],
    python_requires='>=3.6',
    install_requires=[],
)