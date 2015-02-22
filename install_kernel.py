import os
import json
import sys

kernel_json = {
    "argv": ["java", "-jar",
             "/home/alex/ws/IScala/target/scala-2.11/lib/IScala.jar",
             "--profile",
             "{connection_file}",
             "--parent"],
    "display_name": "Scala",
    "language": "scala",
    "name": "scala_kernel",
}


def install_spec():
    user = '--user' in sys.argv
    from IPython.kernel.kernelspec import install_kernel_spec
    from IPython.utils.tempdir import TemporaryDirectory
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)  # Starts off as 700, not user readable
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)
        #log.info('Installing kernel spec')
        try:
            install_kernel_spec(td, "scala_kernel", user=user,
                                replace=True)
        except:
            install_kernel_spec(td, "scala_kernel", user=not user,
                                replace=True)

install_spec()
