"""
GlobalPlatform APIs Package

This package provides access to GlobalPlatform API specifications and binaries
for SmartCard/Secure Element development.
"""
__version__ = "1.0.0"

import os
import importlib.resources
from pathlib import Path


def get_api_resource(api_type, version, filename):
    """
    Get a specific API resource file.
    
    Args:
        api_type (str): The API type (broker, contactless, core, open, scpp, upgrade)
        version (str): The version (e.g., '1.0', '1.8')
        filename (str): The filename to retrieve
    
    Returns:
        str: Path to the resource file
    """
    try:
        # Construct the resource path in the gpapis subdirectory
        resource_path = f"{api_type}/{version}/{filename}"
        # Use importlib.resources to get the resource
        with importlib.resources.path('gpapis', resource_path) as resource_file:
            return str(resource_file)
    except Exception:
        # Fallback to relative path if resource is not found
        return os.path.join(os.path.dirname(__file__), api_type, version, filename)


def list_api_versions(api_type):
    """
    List all available versions for a specific API type.
    
    Args:
        api_type (str): The API type (broker, contactless, core, open, scpp, upgrade)
    
    Returns:
        list: List of available versions
    """
    try:
        # Get the directory listing for the API type
        resource_path = f"{api_type}/"
        # Use importlib.resources to list directory contents
        if hasattr(importlib.resources, 'files'):  # Python 3.9+
            files = importlib.resources.files('gpapis').joinpath(resource_path).iterdir()
            return [item.name for item in files if item.is_dir()]
        else:  # Python 3.8 and earlier
            return importlib.resources.contents('gpapis')
    except Exception:
        # Fallback to file system if resource is not found
        api_dir = os.path.join(os.path.dirname(__file__), api_type)
        if os.path.exists(api_dir):
            return [d for d in os.listdir(api_dir) if os.path.isdir(os.path.join(api_dir, d))]
        return []


def get_all_resources():
    """
    Get all available API resources.
    
    Returns:
        dict: Dictionary with API types as keys and their versions as values
    """
    apis = {}
    for api_type in ['broker', 'contactless', 'core', 'open', 'scpp', 'upgrade']:
        versions = list_api_versions(api_type)
        if versions:
            apis[api_type] = versions
    return apis

__all__ = [
    "get_api_resource",
    "list_api_versions", 
    "get_all_resources",
    "broker",
    "contactless",
    "core",
    "open",
    "scpp",
    "upgrade",
]