#!/bin/sh
# Installs the Chiikawa Dots Pets into the Codex pets folder on macOS and Linux.
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.sh | sh
# Pick specific pets with CHIIKAWA_PETS, for example: CHIIKAWA_PETS="chiikawa usagi" sh install.sh
set -eu

REPO_RAW_URL="https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main"
AVAILABLE_PETS="chiikawa hachiware usagi momonga shisa rakko kurimanju siren furuhonya anoko dekatsuyo"
REQUESTED_PETS=$(printf '%s' "${CHIIKAWA_PETS:-$AVAILABLE_PETS}" | tr ',' ' ')
PETS_ROOT="${CODEX_HOME:-$HOME/.codex}/pets"

for pet_id in $REQUESTED_PETS; do
  case " $AVAILABLE_PETS " in
    *" $pet_id "*) ;;
    *) echo "Unknown pet '$pet_id'. Choose from: $AVAILABLE_PETS" >&2; exit 1 ;;
  esac
  pet_folder="$PETS_ROOT/$pet_id"
  mkdir -p "$pet_folder"
  for file_name in pet.json spritesheet.png; do
    curl -fsSL "$REPO_RAW_URL/pets/$pet_id/$file_name" -o "$pet_folder/$file_name"
  done
  echo "Installed $pet_id -> $pet_folder"
done

echo "Done. Restart Codex and pick the pet from its pet list."
