from conans import ConanFile, CMake


class MysqlConnectorConan(ConanFile):
    name = "mysql-connector-cpp"
    version = "8.0.22"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of MysqlConnector here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "use_pic": [True, False],
    }
    default_options = {"shared": False, "use_pic": False}
    requires = [
        "openssl/1.1.1j@bitwyre/stable",
        "protobuf/3.11.4@bitwyre/stable",
        "ZLib/1.2.11@bitwyre/stable"]
    generators = "cmake"
    exports_sources = "*"
    no_copy_source = True

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_SHARED_LIBS'] = self.options.shared
        cmake.definitions["BUILD_STATIC"] = not self.options.shared
        cmake.definitions['BUILD_TESTING'] = False
        cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.use_pic
        cmake.definitions['OPENSSL_ROOT_DIR'] = self.deps_cpp_info["openssl"].rootpath
        cmake.definitions['PROTOBUF_ROOT_DIR'] = self.deps_cpp_info["protobuf"].rootpath
        cmake.definitions['ZLIB_ROOT'] = self.deps_cpp_info["ZLib"].rootpath
        cmake.definitions['WITH_DOC'] = False
        cmake.definitions['WITH_HEADER_CHECKS'] = False
        cmake.definitions['WITH_JDBC'] = False
        cmake.definitions['WITH_TESTS'] = False
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.info.header_only()
