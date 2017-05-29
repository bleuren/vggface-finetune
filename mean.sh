#!/usr/bin/env sh
EXAMPLE=vggface
DATA=vggface
TOOLS=./build/tools
$TOOLS/compute_image_mean $EXAMPLE/face_train_lmdb \
  $DATA/face_mean.binaryproto
echo "Done."