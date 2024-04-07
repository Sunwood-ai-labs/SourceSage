#!/bin/bash

# dist ディレクトリが存在する場合は削除
if [ -d "dist" ]; then
  echo "Cleaning up dist directory..."
  rm -rf dist/
fi

# ビルド実行
echo "Building distributions..."
python setup.py sdist bdist_wheel

echo "Build complete."
