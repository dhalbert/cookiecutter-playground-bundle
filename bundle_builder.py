"""
A CircuitPython project bundle builder for use with Adafruit Playground guides.

This is meant to be invoked as a GithHub Actions workflow as defined in
.github/workflows/bundle_builder.yml. You can run it manually as `make bundle`.

To customize the contents of your project bundle, edit bundle_manifest.cfg
according to the comments in that file.
"""
from configparser import ConfigParser
import os
from os.path import basename, isdir, isfile
import re
import shutil
import subprocess


MANIFEST = 'bundle_manifest.cfg'

def run(cmd):
    result = subprocess.run(cmd, shell=True, check=True, capture_output=True)
    return result.stdout.decode('utf-8').strip()

# Read the bundle manifest file
config = ConfigParser(allow_no_value=True)
config.read(MANIFEST)
cfg = {
    '8.x': config.get('library_bundle', '8.x', fallback=None),
    '9.x': config.get('library_bundle', '9.x', fallback=None),
    'guide_link': config.get('meta', 'guide_link', fallback=None),
    'lib': [k for (k, v) in config.items('lib')],
    'root': [k for (k, v) in config.items('root')],
}

# Get repository url, name, and commit hash metadata from git
git_remote = run('git config --get remote.origin.url')
git_remote = re.sub(r'git@github\.com:', 'https://github.com/', git_remote)
git_remote = re.sub(r'\.git$', '', git_remote)
repo_name = git_remote.split('/')[-1]
commit = run('git rev-parse --short HEAD')

# prepare file and directory paths
files = {
    'zip':    f'build/{repo_name}-{commit}.zip',
    'readme': f'build/{repo_name}/README.txt',
}
dirs = {
    'root':   f'build/{repo_name}',
    '8.x':    f'build/{repo_name}/CircuitPython 8.x',
    '9.x':    f'build/{repo_name}/CircuitPython 9.x',
    '8_lib':  f'build/{repo_name}/CircuitPython 8.x/lib',
    '9_lib':  f'build/{repo_name}/CircuitPython 9.x/lib',
}

# Create the directory tree of the zip archive
for d in dirs.values():
    os.mkdir(d)

# Stage files into the zip archive directory tree
for src in cfg['root']:
    for dst in [dirs['8.x'], dirs['9.x']]:
        if isfile(src):
            shutil.copy2(src, dst)
        elif isdir(src):
            shutil.copytree(src, f"{dst}/{basename(src)}")
        else:
            raise FileNotFoundError(src)

# Generate the README file
readme = f"""
This is a CircuitPython project bundle for {repo_name}.

To use this bundle, follow the guide at:
{cfg['guide_link']}

Libraries in '{repo_name}/CircuitPython 8.x/lib' came from:
{cfg['8.x']}

Libraries in '{repo_name}/CircuitPython 9.x/lib' came from:
{cfg['9.x']}

The rest of this project's code is from commit {commit} of git repo:
{git_remote}
""".strip()
with open(files['readme'], 'w') as f:
    print(readme, file=f)

# Make the zip file
run(f"cd build; zip -r {basename(files['zip'])} {basename(dirs['root'])}")

# Print an unzip listing for the Actions workflow log
print(run(f"unzip -l {files['zip']}"))
