#!/usr/bin/env bash
set -euo pipefail

# 同步当前仓库 changelog 到 ../chatlab.fun 并提交 docs: changelogs update
# 用法：sync_to_chatlab_fun.sh <source_repo> <target_repo>
SOURCE_REPO="${1:-}"
TARGET_REPO="${2:-}"

if [[ -z "$SOURCE_REPO" || -z "$TARGET_REPO" ]]; then
  echo "错误: 缺少参数。用法: sync_to_chatlab_fun.sh <source_repo> <target_repo>" >&2
  exit 1
fi

SRC_CN="$SOURCE_REPO/docs/changelogs_cn.json"
SRC_EN="$SOURCE_REPO/docs/changelogs_en.json"
DST_CN="$TARGET_REPO/docs/public/cn/changelogs.json"
DST_EN="$TARGET_REPO/docs/public/en/changelogs.json"

# 目标文件必须预先存在，不允许自动创建。
if [[ ! -f "$DST_CN" || ! -f "$DST_EN" ]]; then
  echo "错误: chatlab.fun 目标 changelog 文件不存在，请先手动准备" >&2
  exit 1
fi

if [[ ! -f "$SRC_CN" || ! -f "$SRC_EN" ]]; then
  echo "错误: 源仓库 changelog 文件不存在" >&2
  exit 1
fi

cp "$SRC_CN" "$DST_CN"
cp "$SRC_EN" "$DST_EN"

# 仅提交目标文档文件，避免提交其他改动。
git -C "$TARGET_REPO" add docs/public/cn/changelogs.json docs/public/en/changelogs.json

if git -C "$TARGET_REPO" diff --cached --quiet; then
  echo "错误: chatlab.fun 没有可提交的 changelog 变更" >&2
  exit 1
fi

git -C "$TARGET_REPO" commit -m "docs: changelogs update" >/dev/null

git -C "$TARGET_REPO" rev-parse --short HEAD
