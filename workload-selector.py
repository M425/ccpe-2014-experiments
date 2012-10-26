# Copyright 2012 Anton Beloglazov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os
import random
import shutil

if len(sys.argv) < 4:
    print 'You must specify 3 arguments:'
    print '1. The directory containing workload trace files'
    print '2. The directory to write the selected files to'
    print '3. The number of workload trace files to select'
    sys.exit(1)

src = sys.argv[1]
dest = sys.argv[2]
n = int(sys.argv[3])

try:
    shutil.rmtree(dest)
except os.error:
    pass
os.makedirs(dest)

files = os.listdir(src)
for i in range(n):
    f = random.choice(files)
    files.remove(f)
    shutil.copyfile(os.path.join(src, f),
                    os.path.join(dest, f.replace(' ', '')))

print 'Selected and copied ' + str(n) + \
      ' workload trace files to ' + dest
