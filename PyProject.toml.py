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