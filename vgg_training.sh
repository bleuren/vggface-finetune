#!/usr/bin/env sh
./build/tools/caffe train --solver=vggface/solver.prototxt --weights=VGG_FACE.caffemodel -gpu=0 2>&1 | tee log.txt
