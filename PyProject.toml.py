# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


[tool.poetry]
name = "qed-materialgui"
version = "0.1.0"
description = ""
authors = ["Your Name <tdavis0525@protonmail.com>"]

[tool.poetry.dependencies]
python = "^3.10"
PyQt6 = "^6.5.1"
qmaterialwidgets = "^3.0.0"
numpy = "^1.24.3"
pymongo = "^4.3.3"
mayavi = "^4.8.2"
Pillow = "^9.5.0" # Add Pillow library for image handling

[tool.poetry.dev-dependencies]
pytest = "^7.4.0"

[build-system]
requires = ["poetry-core>=1.0.8"]
build-backend = "poetry.core.masonry.api"