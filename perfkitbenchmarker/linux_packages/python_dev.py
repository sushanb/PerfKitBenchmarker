# Copyright 2018 PerfKitBenchmarker Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Module containing python 2.7 dev installation and cleanup functions."""


def YumInstall(vm):
  """Installs the package on the VM."""
  Install(vm, package=vm.PYTHON_PACKAGE + '-devel')


def Install(vm, package='python-dev'):
  """Installs the package on the VM."""
  # Install python first to get the python setup
  vm.Install('python')
  vm.InstallPackages(package)
