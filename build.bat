@echo off
pyinstaller build.spec
pyinstaller build_upx.spec --upx-dir=upx\
