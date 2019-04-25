import git
import os
import shutil
import subprocess
from mkdocs.plugins import BasePlugin
from shutil import copyfile

class ProtoGen(BasePlugin):

    def on_pre_build(self, markdown, **kwargs):
        cmd = os.getcwd() + "/scripts/setup.sh"
        subprocess.run(cmd, shell=True, universal_newlines=True, check=True)

        tmp = os.getcwd() + "/tmp"

        # remove /tmp
        if os.path.isdir(tmp):
            shutil.rmtree(tmp)

        # clone repository
        os.mkdir(tmp)
        git.Git(tmp).clone("https://github.com/ligato/vpp-agent.git")

        subprocess.run("go build")

        for subdir, dirs, files in os.walk(tmp + "/vpp-agent/api"):
            for file in files:
                ext = os.path.splitext(file)[-1].lower()
                if ext == '.proto':

                    # proto paths
                    ppApi = " --proto_path=" + tmp + "/vpp-agent/api"
                    ppVendor = " --proto_path=" + tmp + "/vpp-agent/vendor"
                    docOut = " --doc_out=" + os.getcwd() + "/docs/generated"

                    cmd = "protoc" + ppApi + ppVendor + docOut + " --doc_opt=markdown," + os.path.splitext(file)[0].lower() + ".md " + os.path.join(subdir, file)

                    print("==> generating from " + os.path.splitext(file)[0].lower())
                    subprocess.run(cmd, shell=True, universal_newlines=True, check=True)




        # remove /tmp
        shutil.rmtree(tmp)


        return markdown
