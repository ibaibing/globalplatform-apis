# GlobalPlatform-APIs
This is a project similar to [oracle_javacard_sdks](https://github.com/martinpaljak/oracle_javacard_sdks.git) and [globalplatform-exports](https://github.com/OpenJavaCard/globalplatform-exports.git), collect and organize all API materials for SE released by GlobalPlatfrom.

- As found from https://globalplatform.org and https://github.com/OpenJavaCard/globalplatform-exports.git
- All content is &copy;&reg;&trade; by GlobalPlatform, and they may be used only as per the provided [license agreement](GP-Specification-License-Agreement.pdf)[This file is from [globalplatform-exports](https://github.com/OpenJavaCard/globalplatform-exports.git)].
- Only necessary binary content usable with [ant-javacard](https://github.com/martinpaljak/ant-javacard).
- Easily usable with platforms other than Windows.
- Intended to be included as a Git submodule.

## Usage

```bat
git submodule add https://github.com/ibaibing/globalplatform-apis.git sdks/gpapis
```



## Config Build.xml

```xml
   <target name="build">
   		<javacard jckit="sdks/jcsdks/jc320v24.1_kit">
   			<cap aid=" 54657374506B67" version="1.1" sources="src" ints="true" strip="true" debug="true" verify="true">
   				<applet class="id.example.Applet" aid="5465737441707000" />
   				<import exps="sdks/gpapis/export_files" jar="sdks/gpapis/com.custom.api.jar"/>
   			</cap>
   		</javacard>
   	</target>
```

## Acknowledgment

- https://globalplatform.org/specs-library/
- https://github.com/OpenJavaCard/globalplatform-exports.git
- https://github.com/martinpaljak/oracle_javacard_sdks.git
- https://github.com/martinpaljak/ant-javacard
