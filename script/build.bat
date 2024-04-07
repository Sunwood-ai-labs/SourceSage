@echo off

REM dist ディレクトリが存在する場合は削除
if exist dist rmdir /s /q dist

REM ビルド実行
echo Building distributions...
python setup.py sdist bdist_wheel

echo Build complete.
