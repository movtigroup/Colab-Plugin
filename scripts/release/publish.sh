#!/usr/bin/env bash
# Release publisher for the movtigroup/colab plugin.
#
# Resolves the version from the plugin manifest, skips already-released
# versions, tags the commit, packages the plugin and creates the GitHub
# Release with generated notes and a plugin zip asset.
#
# Runs inside GitHub Actions (ubuntu-latest): python, zip and gh are
# preinstalled; GH_TOKEN is provided by the workflow.
set -euo pipefail

# --- Resolve version and tag --------------------------------------------
VERSION=$(python -c "import json; print(json.load(open('colab/.zcode-plugin/plugin.json'))['version'])")

SKIP=false
if [[ "${GITHUB_REF_TYPE:-branch}" == "tag" ]]; then
  # Manual tag push: it must match the manifest version.
  TAG="${GITHUB_REF_NAME}"
  if [[ "${TAG}" != "v${VERSION}" ]]; then
    echo "::error::Tag ${TAG} does not match manifest version v${VERSION}"
    exit 1
  fi
else
  # Push to main: tag v<version> if it does not exist yet.
  TAG="v${VERSION}"
  if git rev-parse -q --verify "refs/tags/${TAG}" >/dev/null 2>&1; then
    echo "Tag ${TAG} already exists - nothing to release"
    SKIP=true
  fi
fi
echo "Target release: ${TAG} (manifest version ${VERSION}, skip=${SKIP})"
[[ "${SKIP}" == "true" ]] && exit 0

# --- Tag the current commit ----------------------------------------------
git config user.name "movtigroup-release-bot"
git config user.email "actions@users.noreply.github.com"
git tag -a "${TAG}" -m "colab plugin ${TAG}"
git push origin "${TAG}"

# --- Package and publish --------------------------------------------------
ZIP="colab-plugin-${TAG}.zip"
zip -r "${ZIP}" colab
gh release create "${TAG}" "${ZIP}" \
  --title "Google Colab Tools ${TAG}" \
  --generate-notes \
  --verify-tag
echo "Release ${TAG} published."
