#!/usr/bin/env sh
EXAMPLE=vggface
DATA=vggface
TOOLS=./build/tools
$TOOLS/compute_image_mean $EXAMPLE/train_lmdb \
  $DATA/mean.binaryproto
echo "Done."