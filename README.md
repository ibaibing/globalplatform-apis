# GlobalPlatform-APIs
This is a project similar to [oracle_javacard_sdks](https://github.com/martinpaljak/oracle_javacard_sdks.git) and [globalplatform-exports](https://github.com/OpenJavaCard/globalplatform-exports.git), collect and organize all API materials for SmartCard or SE released by GlobalPlatfrom.

- As found from https://globalplatform.org and https://github.com/OpenJavaCard/globalplatform-exports.git
- All content is &copy;&reg;&trade; by GlobalPlatform, and they may be used only as per the provided [license agreement](GP-Specification-License-Agreement.pdf)[This file is from [globalplatform-exports](https://github.com/OpenJavaCard/globalplatform-exports.git)].
- op201.jar is from https://github.com/martinpaljak/javacard-libraries.git
- Only necessary binary content usable with [ant-javacard](https://github.com/martinpaljak/ant-javacard).
- Easily usable with platforms other than Windows.
- Intended to be included as a Git submodule.
- Now available as a pip-installable Python package from GitHub for easy integration.



## Usage

### Pip Installation from GitHub (New!)

Install the package directly from GitHub using pip:

```bash
pip install git+https://github.com/ibaibing/globalplatform-apis.git
```

Or download the wheel file from the [Releases](https://github.com/ibaibing/globalplatform-apis/releases) page and install it directly:

```bash
pip install gpapis-*.whl
```

After installation, you can access the GlobalPlatform APIs from Python:

```python
import gpapis

# List all available API resources
apis = gpapis.get_all_resources()
print(apis)

# Get a specific API resource
resource_path = gpapis.get_api_resource('core', '1.8', 'gpapi-globalplatform.jar')
print(f"API JAR path: {resource_path}")
```

### Git Submodule Usage (Traditional)

1. You can find the demo project [building-javacard-applet](https://github.com/ibaibing/building-javacard-applet.git) to know how to build JavaCard Applet with Ant-JavaCard.

1. Add a Git submodule to your project.

   ```bash
   git submodule add https://github.com/ibaibing/globalplatform-apis.git sdks/gpapis
   ```

1. Edit the ant Build.xml in your project
```xml
target name="build">
    <javacard jckit="sdks/jcsdks/jc320v24.1_kit">
        <cap aid="54657374506B67" version="1.0" sources="src" ints="true" strip="true" debug="true" verify="true">
            <applet class="id.example.Applet" aid="5465737441707000" />
            <!--Add GP API here-->
            <import exps="sdks/gpapis/CORE/1.5/exports" jar="sdks/gpapis/CORE/1.5/gpapi-globalplatform.jar"/>
        </cap>
    </javacard>
</target>
```

## Acknowledgments

We would like to thank:

- https://globalplatform.org/specs-library/
- https://github.com/OpenJavaCard/globalplatform-exports.git
- https://github.com/martinpaljak/oracle_javacard_sdks.git
- https://github.com/martinpaljak/javacard-libraries.git
- https://github.com/martinpaljak/ant-javacard
